{
  'targets': [
    {
      'target_name': 'bindings',
      'sources': [
        'src/bindings.cc'
      ],
      'dependencies': [
        'deps/xpdf/libxpdf.gyp:xpdf'
      ]
  }]
}
