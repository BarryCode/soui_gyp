
{  
  'includes': [
    '../../../build/win_precompile.gypi',
    'mhook.gypi',
  ],
  'targets': [
    {
      'target_name': 'mhook',
      'type': 'static_library',
      'includes': [ '../../build/common.gypi', ],  
      'dependencies': [ 
      	#'../../utilities/utilities.gyp:*',
      	#'../../third-part/png/png.gyp:*',
       ],
    },
  ],
}

# Local Variables:
# tab-width:2
# indent-tabs-mode:nil
# End:
# vim: set expandtab tabstop=2 shiftwidth=2:
