{
  'variables': { 'target_arch%': 'x64' },
  'target_defaults':{
    'default_configuration': 'Release',
    'configurations' : {
      'Release' : {
        'defines' : ['NDEBUG']
      }
    },
    'include_dirs': [
      'libs/goo',
      'libs/fofi',
      'libs/splash',
      'xpdf',
      'config/<(OS)/<(target_arch)'
    ],
    'defines': ['HAVE_CONFIG_H']
  },
   
  'targets' : [{
     'target_name' : 'goo',
     'product_prefix' : 'lib',
     'type': 'static_library',
     'sources': [
       'libs/goo/FixedPoint.cc',
       'libs/goo/GHash.cc',
       'libs/goo/GList.cc',
       'libs/goo/GString.cc',
       'libs/goo/gfile.cc',
       'libs/goo/gmem.cc',
       'libs/goo/gmempp.cc',
       'libs/goo/parseargs.c'
      ]
    },{
     'target_name' : 'fofi',
     'product_prefix': 'lib',
     'type': 'static_library',
     'sources': [
       'libs/fofi/FoFiBase.cc',
       'libs/fofi/FoFiEncodings.cc',
       'libs/fofi/FoFiIdentifier.cc',
       'libs/fofi/FoFiTrueType.cc',
       'libs/fofi/FoFiType1.cc',
       'libs/fofi/FoFiType1C.cc' 
     ]
    },{
     'target_name': 'splash',
     'product_prefix': 'lib',
     'type': 'static_library',
     'sources': [
       'libs/splash/SplashBitmap.cc',
       'libs/splash/SplashClip.cc',
       'libs/splash/SplashFTFont.cc',
       'libs/splash/SplashFTFontEngine.cc',
       'libs/splash/SplashFTFontFile.cc',
       'libs/splash/SplashFont.cc',
       'libs/splash/SplashFontEngine.cc',
       'libs/splash/SplashFontFile.cc',
       'libs/splash/SplashFontFileID.cc',
       'libs/splash/SplashPath.cc',
       'libs/splash/SplashPattern.cc',
       'libs/splash/SplashScreen.cc',
       'libs/splash/SplashState.cc',
       'libs/splash/SplashXPath.cc',
       'libs/splash/SplashXPathScanner.cc'
     ]
    },{
     'target_name': 'xpdf',
     'product_prefix': 'lib',
     'type': 'static_library',
     'sources': [
       'xpdf/AcroForm.cc',
       'xpdf/Annot.cc',
       'xpdf/Array.cc',
       'xpdf/BuiltinFont.cc',
       'xpdf/BuiltinFontTables.cc',
       'xpdf/Catalog.cc',
       'xpdf/CharCodeToUnicode.cc',
       'xpdf/CMap.cc',
       'xpdf/Decrypt.cc',
       'xpdf/Dict.cc',
       'xpdf/Error.cc',
       'xpdf/FontEncodingTables.cc',
       'xpdf/Form.cc',
       'xpdf/Function.cc',
       'xpdf/Gfx.cc',
       'xpdf/GfxFont.cc',
       'xpdf/GfxState.cc',
       'xpdf/GlobalParams.cc',
       'xpdf/JArithmeticDecoder.cc',
       'xpdf/JBIG2Stream.cc',
       'xpdf/JPXStream.cc',
       'xpdf/Lexer.cc',
       'xpdf/Link.cc',
       'xpdf/NameToCharCode.cc',
       'xpdf/OptionalContent.cc',
       'xpdf/Outline.cc',
       'xpdf/Object.cc',
       'xpdf/OutputDev.cc',
       'xpdf/Page.cc',
       'xpdf/Parser.cc',
       'xpdf/PDFDoc.cc',
       'xpdf/PDFDocEncoding.cc',
       'xpdf/PreScanOutputDev.cc',
       'xpdf/PSOutputDev.cc',
       'xpdf/PSTokenizer.cc',
       'xpdf/SecurityHandler.cc',
       'xpdf/SplashOutputDev.cc',
       'xpdf/Stream.cc',
       'xpdf/TextString.cc',
       'xpdf/UnicodeMap.cc',
       'xpdf/XFAForm.cc',
       'xpdf/XpdfPluginAPI.cc',
       'xpdf/XRef.cc',
       'xpdf/Zoox.cc'
     ],
     'dependencies' : [
       'goo',
       'splash',
       'fofi'
     ],
     'direct_dependent_settings': {
       'include_dirs': [
          'libs/goo',
          'libs/splash',
          'xpdf',
          'config/<(OS)/<(target_arch)'
       ]
     }
    },{
     'target_name': 'pdfinfo',
     'type': 'executable',
     'dependencies': ['xpdf'],
     'sources': [
       'xpdf/pdfinfo.cc'
      ]
    }
   ]
}
