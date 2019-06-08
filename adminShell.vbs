Set oShell = CreateObject("Shell.Application")
oShell.ShellExecute "cmd.exe", , , "runas", 1
Set objWshShell = WScript.CreateObject("WScript.Shell")
WScript.Sleep 2000
objWshShell.SendKeys "{LEFT}"
objWshShell.SendKeys "{ENTER}"