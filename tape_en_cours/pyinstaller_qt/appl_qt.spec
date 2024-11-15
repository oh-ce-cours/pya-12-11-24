# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['application_qt.py'],
             pathex=['/Users/matthieufalce/Desktop/pya-12-11-24/tape_en_cours/pyinstaller_qt/dist'],
             binaries=[],
             datas=[("/Users/matthieufalce/Desktop/pya-12-11-24/tape_en_cours/pyinstaller_qt/window_handle_templating.ui", ".")],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='WinFileGenerator',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
