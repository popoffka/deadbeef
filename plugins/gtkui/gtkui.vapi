[CCode (cprefix = "Gtkui", lower_case_cprefix = "gtkui_")]
namespace Gtkui {
	[CCode (cheader_filename = "drawing.h")]
        public static unowned Gdk.Color get_bar_foreground_color ();
        public static unowned Gdk.Color get_bar_background_color ();
        public static unowned void init_theme_colors ();
}
[CCode (cheader_filename = "gtkui.h")]
public static unowned void seekbar_draw(Gtk.Widget *widget);
public static unowned bool on_seekbar_button_press_event(Gtk.Widget widget, Gdk.EventButton event);
public static unowned bool on_seekbar_button_release_event(Gtk.Widget widget, Gdk.EventButton event);
public static unowned bool on_seekbar_motion_notify_event(Gtk.Widget widget, Gdk.EventMotion event);

