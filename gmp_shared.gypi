#
# gmp_shared.gypi
#
#{
#  'targets': [
#    {
#      'target_name': 'gmp_shared',
#      'type': 'shared_library',
#      'product_name': 'gmp',
#      'export_dependent_settings': [
#        'gmp_static',
#      ],
#      'dependencies': [
#        'gmp_static',
#      ],
#      'conditions': [
#        ['OS=="win"', {
#          'product_name': 'gmp',
#          'sources': [
#          ],
#        }], # OS="win"
#      ],
#    }
#  ],
#}
# vim:sts=2:sw=2:norl
