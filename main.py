#!/usr/bin/env python3

import gi
import cairo
import psutil
from quoters import Quote
from datetime import datetime
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GLib, Pango

class QuoteApp(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_type_hint(Gdk.WindowTypeHint.DOCK)
        self.set_keep_below(True)
        self.set_decorated(False)
        self.set_app_paintable(True)
        self.connect("destroy", Gtk.main_quit)

        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(self.box)

        # Create a label to display the quote
        self.quote_label = Gtk.Label()
        self.quote_label.set_line_wrap(True)
        self.quote_label.set_justify(Gtk.Justification.CENTER)
        self.quote_label.set_halign(Gtk.Align.CENTER)
        self.quote_label.set_valign(Gtk.Align.CENTER)

        font_desc = Pango.FontDescription("Sans 24")
        self.quote_label.modify_font(font_desc)

        self.box.pack_start(self.quote_label, True, True, 0)

        # Create a label to display the digital clock
        self.clock_label = Gtk.Label()
        self.clock_label.set_line_wrap(True)
        self.clock_label.set_justify(Gtk.Justification.CENTER)
        self.clock_label.set_halign(Gtk.Align.CENTER)
        self.clock_label.set_valign(Gtk.Align.CENTER)

        # Increase the font size for the clock text
        font_desc = Pango.FontDescription("Sans 24")
        self.clock_label.modify_font(font_desc)

        # Create a label to display the battery percentage
        self.battery_label = Gtk.Label()
        self.battery_label.set_line_wrap(True)
        self.battery_label.set_justify(Gtk.Justification.CENTER)
        self.battery_label.set_halign(Gtk.Align.CENTER)
        self.battery_label.set_valign(Gtk.Align.END)  # Align to the bottom of the window

        # Increase the font size for the battery text
        font_desc = Pango.FontDescription("Sans 16")
        self.battery_label.modify_font(font_desc)

        self.box.pack_start(self.clock_label, True, True, 0)
        self.box.pack_start(self.battery_label, True, True, 0)

        self.set_position(Gtk.WindowPosition.CENTER_ALWAYS)

        screen = self.get_screen()
        visual = screen.get_rgba_visual()
        if visual is not None and screen.is_composited():
            self.set_visual(visual)

        self.update_quote()
        self.update_battery()
        self.update_clock()  # Start updating the digital clock

    def set_random_quote(self):
        quote_text = Quote.print_programming_quote()
        words = quote_text.split()
        lines = []
        current_line = []

        for word in words:
            current_line.append(word)
            if len(current_line) >= 12:
                lines.append(" ".join(current_line))
                current_line = []

        if current_line:
            lines.append(" ".join(current_line))

        formatted_quote = "\n".join(lines)
        self.quote_label.set_text(formatted_quote)

    def update_quote(self):
        self.set_random_quote()
        GLib.timeout_add(10000, self.update_quote)

    def update_clock(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        self.clock_label.set_text(current_time)

        GLib.timeout_add(1000, self.update_clock)  # Update the clock every second

    def update_battery(self):
        battery = psutil.sensors_battery()
        if battery:
            percent = int(round(battery.percent))
            battery_status = "Charging" if battery.power_plugged else "Discharging"
            battery_text = f"{percent}% ({battery_status})"
        else:
            battery_text = "Battery information not available"

        self.battery_label.set_text(battery_text)

        GLib.timeout_add(10000, self.update_battery)

    def on_draw(self, widget, context):
        context.set_source_rgba(0, 0, 0, 0)
        context.set_operator(cairo.Operator.SOURCE)
        context.paint()
        context.set_operator(cairo.Operator.OVER)

def main():
    win = QuoteApp()
    win.show_all()
    Gtk.main()

if __name__ == "__main__":
    main()
