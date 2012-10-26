#
# gmp-5.0.5-patch.gyp
#
{
  'targets': [
    {
      'target_name': 'gmp-5.0.5-patch',
      'type': 'none',
      'direct_dependent_settings': {
        'include_dirs': [
          '<(SHARED_INTERMEDIATE_DIR)/',
        ],
      },
      'dependencies': [
        'configure.gyp:*',
      ],
      'copies': [
        {
          'destination': '<(SHARED_INTERMEDIATE_DIR)',
          'files': [
            '../gmp-5.0.5/mpn/x86/gmp-mparam.h',
          ],
        },
      ],
      'actions': [
        {
          'variables': {
            'fakeconf': '<(SHARED_INTERMEDIATE_DIR)/fakeconf.exe',
            'source': '../gmp-5.0.5/gmp-h.in',
            'destination': '<(SHARED_INTERMEDIATE_DIR)/gmp.h',
          },
          'action_name': 'convert gmp-h.in to gmp.h',
          'inputs': [
            '<(fakeconf)',
            '<(source)',
          ],
          'outputs': [
            '<(destination)',
          ],
          'action': ['<(fakeconf)', '<(source)', '<(destination)'],
          'msvs_cygwin_shell': 0,
        },
        {
          'variables': {
            'fakeconf': '<(SHARED_INTERMEDIATE_DIR)/fakeconf.exe',
            'source': '../gmp-5.0.5/config.in',
            'destination': '<(SHARED_INTERMEDIATE_DIR)/config.h',
          },
          'action_name': 'convert config.in to config.h',
          'inputs': [
            '<(fakeconf)',
            '<(source)',
          ],
          'outputs': [
            '<(destination)',
          ],
          'action': ['<(fakeconf)', '<(source)', '<(destination)'],
          'msvs_cygwin_shell': 0,
        },
        {
          'variables': {
            'pipecurry': 'pipecurry.bat',
            'gen-fib': '<(SHARED_INTERMEDIATE_DIR)/gen-fib.exe',
            'destination': '<(SHARED_INTERMEDIATE_DIR)/fib_table.h',
            'GMP_LIMB_BITS': '32',
            'GMP_NAIL_BITS': '0',
          },
          'action_name': 'generate <(destination)',
          'inputs': [
            '<(pipecurry)',
            '<(gen-fib)',
          ],
          'outputs': [
            '<(destination)',
          ],
          'action': [
            '<(pipecurry)', '<(destination)',
            '<(gen-fib)', 'header',
            '<(GMP_LIMB_BITS)', '<(GMP_NAIL_BITS)',
          ],
          'msvs_cygwin_shell': 0,
        },
        {
          'variables': {
            'pipecurry': 'pipecurry.bat',
            'gen-fib': '<(SHARED_INTERMEDIATE_DIR)/gen-fib.exe',
            'destination': '<(SHARED_INTERMEDIATE_DIR)/fib_table.c',
            'GMP_LIMB_BITS': '32',
            'GMP_NAIL_BITS': '0',
          },
          'action_name': 'generate <(destination)',
          'inputs': [
            '<(pipecurry)',
            '<(gen-fib)',
          ],
          'outputs': [
            '<(destination)',
          ],
          'action': [
            '<(pipecurry)', '<(destination)',
            '<(gen-fib)', 'table',
            '<(GMP_LIMB_BITS)', '<(GMP_NAIL_BITS)',
          ],
          'msvs_cygwin_shell': 0,
        },
        {
          'variables': {
            'pipecurry': 'pipecurry.bat',
            'gen-bases': '<(SHARED_INTERMEDIATE_DIR)/gen-bases.exe',
            'destination': '<(SHARED_INTERMEDIATE_DIR)/mp_bases.h',
            'GMP_LIMB_BITS': '32',
            'GMP_NAIL_BITS': '0',
          },
          'action_name': 'generate <(destination)',
          'inputs': [
            '<(pipecurry)',
            '<(gen-bases)',
          ],
          'outputs': [
            '<(destination)',
          ],
          'action': [
            '<(pipecurry)', '<(destination)',
            '<(gen-bases)', 'header',
            '<(GMP_LIMB_BITS)', '<(GMP_NAIL_BITS)',
          ],
          'msvs_cygwin_shell': 0,
        },
        {
          'variables': {
            'pipecurry': 'pipecurry.bat',
            'gen-bases': '<(SHARED_INTERMEDIATE_DIR)/gen-bases.exe',
            'destination': '<(SHARED_INTERMEDIATE_DIR)/mp_bases.c',
            'GMP_LIMB_BITS': '32',
            'GMP_NAIL_BITS': '0',
          },
          'action_name': 'generate <(destination)',
          'inputs': [
            '<(pipecurry)',
            '<(gen-bases)',
          ],
          'outputs': [
            '<(destination)',
          ],
          'action': [
            '<(pipecurry)', '<(destination)',
            '<(gen-bases)', 'table',
            '<(GMP_LIMB_BITS)', '<(GMP_NAIL_BITS)',
          ],
          'msvs_cygwin_shell': 0,
        },
        {
          'variables': {
            'pipecurry': 'pipecurry.bat',
            'gen-fac_ui': '<(SHARED_INTERMEDIATE_DIR)/gen-fac_ui.exe',
            'destination': '<(SHARED_INTERMEDIATE_DIR)/fac_ui.h',
            'GMP_LIMB_BITS': '32',
            'GMP_NAIL_BITS': '0',
          },
          'action_name': 'generate <(destination)',
          'inputs': [
            '<(pipecurry)',
            '<(gen-fac_ui)',
          ],
          'outputs': [
            '<(destination)',
          ],
          'action': [
            '<(pipecurry)', '<(destination)',
            '<(gen-fac_ui)',
            '<(GMP_LIMB_BITS)', '<(GMP_NAIL_BITS)',
          ],
          'msvs_cygwin_shell': 0,
        },
        {
          'variables': {
            'pipecurry': 'pipecurry.bat',
            'gen-psqr': '<(SHARED_INTERMEDIATE_DIR)/gen-psqr.exe',
            'destination': '<(SHARED_INTERMEDIATE_DIR)/perfsqr.h',
            'GMP_LIMB_BITS': '32',
            'GMP_NAIL_BITS': '0',
          },
          'action_name': 'generate <(destination)',
          'inputs': [
            '<(pipecurry)',
            '<(gen-psqr)',
          ],
          'outputs': [
            '<(destination)',
          ],
          'action': [
            '<(pipecurry)', '<(destination)',
            '<(gen-psqr)',
            '<(GMP_LIMB_BITS)', '<(GMP_NAIL_BITS)',
          ],
          'msvs_cygwin_shell': 0,
        },
      ],
    },
  ],
}
# vim:sts=2:sw=2:norl
