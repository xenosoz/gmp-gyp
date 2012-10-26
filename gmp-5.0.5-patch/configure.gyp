#
# configure.gyp
#
{
  'targets': [
    {
      'target_name': 'fakeconf',
      'product_dir': '<(SHARED_INTERMEDIATE_DIR)',
      'type': 'executable',
      'sources': [
        'src/fakeconf.cpp',
      ],
    },
    {
      'target_name': 'gen-fib',
      'product_dir': '<(SHARED_INTERMEDIATE_DIR)',
      'type': 'executable',
      'sources': [
        '../gmp-5.0.5/gen-fib.c',
      ],
    },
    {
      'target_name': 'gen-bases',
      'product_dir': '<(SHARED_INTERMEDIATE_DIR)',
      'type': 'executable',
      'sources': [
        '../gmp-5.0.5/gen-bases.c',
      ],
    },
    {
      'target_name': 'gen-fac_ui',
      'product_dir': '<(SHARED_INTERMEDIATE_DIR)',
      'type': 'executable',
      'sources': [
        '../gmp-5.0.5/gen-fac_ui.c',
      ],
    },
    {
      'target_name': 'gen-psqr',
      'product_dir': '<(SHARED_INTERMEDIATE_DIR)',
      'type': 'executable',
      'sources': [
        '../gmp-5.0.5/gen-psqr.c',
      ],
    },
  ],
}
# vim:sts=2:sw=2:norl
