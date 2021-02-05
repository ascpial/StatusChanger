# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['C:/Users/El├¿ve/Desktop/Discord/Discord RPC/main.py'],
             pathex=['C:\\Users\\Elève\\Desktop\\Discord\\Discord RPC'],
             binaries=[],
             datas=[('C:/Users/El├¿ve/Desktop/Discord/Discord RPC/flag_fr.png', '.'), ('C:/Users/El├¿ve/Desktop/Discord/Discord RPC/flag_gb.png', '.'), ('C:/Users/El├¿ve/Desktop/Discord/Discord RPC/StatusChanger.ico', '.')],
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
          [],
          exclude_binaries=True,
          name='StatusChanger',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False , icon='C:\\Users\\El├¿ve\\Desktop\\Discord\\Discord RPC\\StatusChanger.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='StatusChanger')
