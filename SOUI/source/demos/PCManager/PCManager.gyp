
{  
  'includes': [
    '../../../build/win_precompile.gypi',
    'PCManager.gypi',
  ],
  'targets': [
    {
      'target_name': 'PCManager',
      'type': 'executable',
      'includes': [ '../../build/common.gypi', ],  
      'dependencies': [  
					'<(app_root)/utilities/utilities.gyp:*',
      		'<(app_root)/SOUI/SOUI.gyp:*',
      		'<(app_root)/third-part/third-part.gyp:*',      		
      	  '<(app_root)/components/components.gyp:*',
      ],
    },
  ],
}

# Local Variables:
# tab-width:2
# indent-tabs-mode:nil
# End:
# vim: set expandtab tabstop=2 shiftwidth=2:
