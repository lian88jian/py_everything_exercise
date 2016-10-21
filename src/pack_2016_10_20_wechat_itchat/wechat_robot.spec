# -*- mode: python -*-

block_cipher = None


a = Analysis(['wechat_robot.py'],
             pathex=['F:\\dev\\python\\3.5.2', 'F:\\dev\\python\\3.5.2\\DLLs', 'F:\\dev\\python\\3.5.2\\Lib', 'F:\\dev\\python\\3.5.2\\Scripts', 'F:\\dev\\eclipse_python\\workspace\\Everything\\src\\pack_2016_10_20_wechat_itchat'],
             binaries=None,
             datas=None,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='wechat_robot',
          debug=False,
          strip=False,
          upx=True,
          console=True )
