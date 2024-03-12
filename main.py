# import cmd
#
# class MyShell(cmd.Cmd):
#     prompt = "(my_shell) "
#
#     def do_list(self, arg):
#         print("Listing items...")
#         return False  # Don't terminate the loop after list command
#
#     def do_exit(self, arg):
#         print("Exiting my shell.")
#         return True  # Terminate the loop
#
# if __name__ == "__main__":
#     my_shell = MyShell()
#
#     # Execute a single "list" command
#     my_shell.onecmd("list")
#
#     # Continue with the interactive loop
#     my_shell.cmdloop()

#-------------------------------------------------------------
# import cmd
#
# class MyShell(cmd.Cmd):
#     prompt = "(my_shell) "
#
#     def do_list(self, arg):
#         print("Listing items...")
#
#     def precmd(self, line):
#         return line.strip()  # Remove leading/trailing whitespace
#
# if __name__ == "__main__":
#     MyShell().cmdloop()

#-------------------------------------------------------------
#
# import cmd
#
# class MyShell(cmd.Cmd):
#     prompt = "(my_shell) "
#
#     def do_list(self, arg):
#         print("Listing items...")
#
#     def postcmd(self, stop, line):
#         print("Finished command:", line)
#         return stop  # Pass on the stop signal
#
# if __name__ == "__main__":
#     MyShell().cmdloop()
#-------------------------------------------------------------

# import cmd
#
# class MyShell(cmd.Cmd):
#     intro = None  # Override default intro message
#
#     def preloop(self):
#         self.intro = "Welcome to my custom shell!\n"
#         self.config = {"theme": "dark"}  # Example configuration
#
#     def do_list(self, arg):
#         print("Listing items...")
#
#     def do_exit(self, args):
#         return  True
#
#     def postloop(self):
#         print("Exiting my shell. Goodbye!")
#
# if __name__ == "__main__":
#     MyShell().cmdloop()
#-------------------------------------------------------------

# import cmd
#
# class MyShell(cmd.Cmd):
#     prompt = "(my_shell) "
#
#     def do_list(self, arg):
#         print("Listing items...")
#
#     def emptyline(self):
#         print("Please enter a command. Type 'help' for a list of commands.")
#         return True  # Continue the loop
#
# if __name__ == "__main__":
#     MyShell().cmdloop()
#-------------------------------------------------------------

# import cmd
#
# class MyShell(cmd.Cmd):
#     prompt = "(my_shell) "
#
#     def do_list(self, arg):
#         print("Listing items...")
#
#     def do_show(self, arg):
#         print("Showing details...")
#
#     def default(self, line):
#         print(f"Unknown command: '{line}'. Did you mean 'list' or 'show'?")
#         return True  # Continue the loop
#
# if __name__ == "__main__":
#     MyShell().cmdloop()

#-------------------------------------------------------------

# import cmd
#
# class MyShell(cmd.Cmd):
#     prompt = "(my_shell) "
#
#     def do_list(self, arg):
#         print(f"Listing items with filter: {arg}")
#
#     def complete_list(self, text, line):
#         # Offer completions for filter options (e.g., "all", "active")
#         options = ["all", "active", "completed"]
#         return [o for o in options if o.startswith(text)]
#
# if __name__ == "__main__":
#     MyShell().cmdloop()

#-------------------------------------------------------------
# import cmd
#
# class MyShell(cmd.Cmd):
#     prompt = "(my_shell) "
#
#     def do_list(self, arg):
#         print("Listing items...")
#
#     def do_show(self, arg):
#         print("Showing details...")
#
#     def completedefault(self, text, line, begidx, endidx):
#         commands = [c for c in dir(self) if c.startswith("do_")]  # Get all "do_" methods (commands)
#         return [c[3:] for c in commands if c.startswith("do_") and c[3:].startswith(text)]  # Extract command names
#
# if __name__ == "__main__":
#     MyShell().cmdloop()

#-------------------------------------------------------------
# import cmd
#
# class MyShell(cmd.Cmd):
#     prompt = "(my_shell) "
#
#     def do_list(self, arg):
#         print("Listing items...")
#
#     def do_show(self, arg):
#         print(f"Showing details for: {arg}")
#
# if __name__ == "__main__":
#     my_shell = MyShell()
#
#     # User enters "list all"
#     cmd_name, args = my_shell.parseline("list all")
#     # cmd_name will be "list", args will be "all"
#
#     # User presses Enter without a command
#     cmd_name, args = my_shell.parseline("")
#     # cmd_name will be "", args will be ""
#-------------------------------------------------------------

# import cmd
#
# class MyShell(cmd.Cmd):
#     prompt = "(my_shell) "
#
#     def do_list(self, arg):
#         print(f"Listing items with filter: {arg}")
#
#     def complete_list(self, text, line):
#         # Offer completions for filter options
#         options = ["all", "active", "completed"]
#         return [o for o in options if o.startswith(text)]
#
#     def help_list(self):
#         print("The 'list' command displays items. You can optionally filter results:")
#         print("  list [all | active | completed]")
#
# if __name__ == "__main__":
#     MyShell().cmdloop()
#-------------------------------------------------------------

# import cmd
#
# class MyShell(cmd.Cmd):
#     prompt = "(my_shell) "
#
#     def do_list(self, arg):
#         print("Listing items...")
#
#     def do_show(self, arg):
#         print(f"Showing details for: {arg}")
#
#     def help_list(self):
#         print("The 'list' command displays items.")
#
#     def complete_help(self, text, line):
#         # Get a list of all available help topics/commands (e.g., from method names)
#         help_topics = [topic for topic in dir(self) if topic.startswith("help_")]
#         return [t for t in help_topics if t.startswith(text)]
#
#     def do_help(self, arg):
#         # Check for specific help topic
#         if arg:
#             help_method = getattr(self, f"help_{arg}", None)
#             if help_method:
#                 help_method()
#                 return
#         # Display list of available help topics or generic message
#         print("Type 'help <topic>' for specific help.")
#         print("Available help topics:")
#         for topic in dir(self) if topic.startswith("help_"):
#             print(f"  - {topic[5:]}")
#
# if __name__ == "__main__":
#     MyShell().cmdloop()

#-------------------------------------------------------------
# import cmd
#
# class MyShell(cmd.Cmd):
#     # ... your command handler methods (do_<command_name>)
#
#     def get_available_commands(self):
#         # Get a list of all methods starting with "do_" (assuming those are commands)
#         return [method[3:] for method in dir(self) if method.startswith("do_")]
#
# if __name__ == "__main__":
#     my_shell = MyShell()
#     available_commands = my_shell.get_available_commands()
#     print("Available commands:", available_commands)

#-------------------------------------------------------------

# import cmd
# from textwrap import wrap
#
# class MyShell(cmd.Cmd):
#     intro = "Welcome to my custom shell!\n"
#
#     def print_topics(self, header, cmds, cmdlen, maxcol=80):
#         """Overridden print_topics method for columnized output."""
#         if cmds:  # Check if there are topics to print
#             # Format topics into columns (adjust maxcol and wrap width as needed)
#             formatted_topics = "\n".join(
#                 "\t".join(wrap(topic, maxcol - len(header) - 4))
#                 for topic in cmds
#             )
#             print(header + "\n" + formatted_topics)
#         else:
#             print("No topics or commands available.")
#
#     # ... other methods (do_<command_name>, etc.)
#-------------------------------------------------------------
# import cmd
#
# class MyShell(cmd.Cmd):
#     intro = "Welcome to MyShell!\n"
#     doc_leader = "** (Admin Command): **"  # Prefix for admin commands
#     doc_header = "Available Commands:"
#     misc_header = "Help Topics:"
#     undoc_header = "Commands without Help:"
#     ruler = '-' * 50
#     nohelp = "No detailed help available for '%s'. Use 'help' for a list of commands."
#
#     def do_list(self, arg):
#         """Lists all available items."""
#         print("Listing items...")
#
#     def do_admin_command(self, arg):
#         """Performs an administrative action.
#
#         (Requires administrator privileges)
#         """
#         print("Executing admin command...")
#
# if __name__ == "__main__":
#     MyShell().cmdloop()

#-------------------------------------------------------------
# import datetime

# Today's date and time
# now = datetime.datetime.now()
# print(now)  # Output: 2024-03-11 17:34:22.730258
#
# # Specific date and time
# specific_datetime = datetime.datetime(2023, 12, 31, 23, 59, 59)
# print(specific_datetime)  # Output: 2023-12-31 23:59:59
#-------------------------------------------------------------

# year = now.year
# month = now.month
# day = now.day
# hour = now.hour
# minute = now.minute
# second = now.second
# microsecond = now.microsecond
#
# print("Year:", year)  # Output: Year: 2024
# print("Month:", month)  # Output: Month: 3
# # ... and so on for other components
#-------------------------------------------------------------

# Common format specifiers:
# %Y: Full year (e.g., 2024)
# %m: Month as a zero-padded decimal number (01-12)
# %d: Day of the month as a zero-padded decimal number (01-31)
# %H: Hour in 24-hour format (00-23)
# %M: Minute as a zero-padded decimal number (00-59)
# %S: Second as a zero-padded decimal number (00-59)

# formatted_date = now.strftime("%Y-%m-%d")
# print(formatted_date)  # Output: 2024-03-11
#
# formatted_time = now.strftime("%H:%M:%S")
# print(formatted_time)  # Output: 17:34:22
#
# # Custom format
# custom_format = now.strftime("%A, %B %d, %Y")
# print(custom_format)  # Output: Monday, March 11, 2024 (e.g., Day of the week, Month name, Day)
#-------------------------------------------------------------

# # Calculate time difference between two datetimes
# one_day = datetime.timedelta(days=1)
# tomorrow = now + one_day
# time_diff = tomorrow - now
# print(time_diff)  # Output: 1 day, 0:00:00
#
# # Accessing components of timedelta
# print(time_diff.days)  # Output: 1
# print(time_diff.seconds)  # Output: 0
# print(time_diff.microseconds)  # Output: 0

#-------------------------------------------------------------

# # Install pytz: pip install pytz
# import pytz
#
# # Get local timezone
# local_timezone = pytz.timezone('US/Eastern')  # Replace with your
#-------------------------------------------------------------

# # Add 30 days to today
# thirty_days_from_now = now + datetime.timedelta(days=30)
# print(thirty_days_from_now)
#
# # Subtract 2 hours from now
# two_hours_ago = now - datetime.timedelta(hours=2)
# print(two_hours_ago)
#-------------------------------------------------------------

# print(datetime.time())
# print(datetime.datetime.fromisocalendar(2020, 1, 2))
# print(datetime.datetime.isoformat(datetime.datetime.now()))
# print(datetime.datetime.isocalendar(datetime.datetime.now()))
#-------------------------------------------------------------

