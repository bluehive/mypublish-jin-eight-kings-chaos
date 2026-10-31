#!/usr/bin/env python3
"""Build a horizontal EPUB preview from the chapter drafts using Pandoc."""
import argparse
import shutil
import subprocess
import zipfile
import xml.etree.ElementTree as ET

from combine_drafts import BOOK, ROOT, SLUG, combine_text


def verify(epub):
    if BOOK.read_text(encoding='utf-8') != combine_text():
        raise SystemExit('FAIL: draft → book.md の鮮度不一致')
    with zipfile.ZipFile(epub) as archive:
        if archive.testzip() is not None:
            raise SystemExit('FAIL: EPUB ZIP corruption')
        first = archive.infolist()[0]
        if (first.filename != 'mimetype' or first.compress_type != zipfile.ZIP_STORED
                or archive.read('mimetype') != b'application/epub+zip'):
            raise SystemExit('FAIL: EPUB mimetype')
        container = ET.fromstring(archive.read('META-INF/container.xml'))
        package_path = container.find('.//{*}rootfile').attrib['full-path']
        package = ET.fromstring(archive.read(package_path))
        items = package.findall('.//{*}manifest/{*}item')
        if not any('nav' in item.attrib.get('properties', '').split() for item in items):
            raise SystemExit('FAIL: EPUB navigation missing')
        for name in archive.namelist():
            if name.endswith(('.xml', '.opf', '.xhtml', '.ncx')):
                ET.fromstring(archive.read(name))
    print('PASS: draft → book.md / EPUB ZIP・XML・目次（今回生成分）')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--format', choices=['epub-horizontal'], default='epub-horizontal')
    parser.add_argument('--no-cover', action='store_true', help='表紙なし（既定）')
    parser.add_argument('--verify', action='store_true')
    args = parser.parse_args()
    pandoc = shutil.which('pandoc')
    if not pandoc:
        raise SystemExit('Pandoc 3以上をインストールし PATH に追加してください。')
    BOOK.parent.mkdir(parents=True, exist_ok=True)
    BOOK.write_text(combine_text(), encoding='utf-8')
    output = ROOT / 'output' / SLUG / '晋・八王の乱と混沌-横書き.epub'
    output.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run([
        pandoc, str(BOOK), '--from=markdown', '--to=epub3', '--toc', '--toc-depth=2',
        '--css', str(ROOT / 'assets/epub/style-horizontal.css'),
        '--resource-path', str(ROOT), '--output', str(output),
    ], check=True, cwd=ROOT)
    if args.verify:
        verify(output)
    print(f'Generated {output.relative_to(ROOT)}（執筆準備版）')


if __name__ == '__main__':
    main()
