@echo off

powershell -Command "& {Add-Type -AssemblyName System.Windows.Forms; [System.Windows.Forms.MessageBox]::Show('Success', 'Simple Security', 'OK', [System.Windows.Forms.MessageBoxIcon]::Information);}"