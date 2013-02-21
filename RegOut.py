import sublime, sublime_plugin

class RegOutCommand( sublime_plugin.WindowCommand ):
	def run( self ):
		self.window.show_input_panel( "RegOut - Regular Expression:", "", self.on_done, None, None )

	def on_done( self, regex ):
		current = self.window.active_view()
		new = self.window.new_file()

		hits = current.find_all( regex )

		edit = new.begin_edit()
		for hit in hits:
			new.insert( edit, new.size(), current.substr( hit ) )
			new.insert( edit, new.size(), '\n\n-----------------------------\n\n' )

		new.end_edit( edit )
