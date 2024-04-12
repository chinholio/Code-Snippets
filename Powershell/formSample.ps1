# Load necessary .NET Framework classes
Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing

# Create a new form
$form = New-Object System.Windows.Forms.Form
$form.Text = 'PowerShell GUI Example'
$form.Size = New-Object System.Drawing.Size(500, 300)
$form.StartPosition = 'CenterScreen'

# Add a label to instruct the user
$label = New-Object System.Windows.Forms.Label
$label.Location = New-Object System.Drawing.Point(10, 20)
$label.Size = New-Object System.Drawing.Size(280, 20)
$label.Text = 'Please enter the information in the space below:'
$form.Controls.Add($label)

# Add a text box for free text input
$textBox = New-Object System.Windows.Forms.TextBox
$textBox.Location = New-Object System.Drawing.Point(10, 40)
$textBox.Size = New-Object System.Drawing.Size(260, 20)
$form.Controls.Add($textBox)

# Add radio buttons for options
$radioButton1 = New-Object System.Windows.Forms.RadioButton
$radioButton1.Location = New-Object System.Drawing.Point(10, 70)
$radioButton1.Text = 'Option 1'
$form.Controls.Add($radioButton1)

$radioButton2 = New-Object System.Windows.Forms.RadioButton
$radioButton2.Location = New-Object System.Drawing.Point(10, 90)
$radioButton2.Text = 'Option 2'
$form.Controls.Add($radioButton2)

# Add a drop-down list (combo box)
$comboBox = New-Object System.Windows.Forms.ComboBox
$comboBox.Location = New-Object System.Drawing.Point(10, 120)
$comboBox.Items.AddRange('Item 1', 'Item 2', 'Item 3')
$form.Controls.Add($comboBox)

# Add a button to open a folder selection dialog
$folderButton = New-Object System.Windows.Forms.Button
$folderButton.Location = New-Object System.Drawing.Point(10, 150)
$folderButton.Text = 'Select Folder'
$folderButton.Add_Click({
    $folderDialog = New-Object System.Windows.Forms.FolderBrowserDialog
    if ($folderDialog.ShowDialog() -eq [System.Windows.Forms.DialogResult]::OK) {
        $selectedFolder = $folderDialog.SelectedPath
        # You can use $selectedFolder as needed
    }
})
$form.Controls.Add($folderButton)

# Add a check box
$checkBox = New-Object System.Windows.Forms.CheckBox
$checkBox.Location = New-Object System.Drawing.Point(10, 180)
$checkBox.Text = 'Check this box'
$form.Controls.Add($checkBox)

# Add an OK button
$okButton = New-Object System.Windows.Forms.Button
$okButton.Location = New-Object System.Drawing.Point(75, 220)
$okButton.Text = 'OK'
$okButton.DialogResult = [System.Windows.Forms.DialogResult]::OK
$form.AcceptButton = $okButton
$form.Controls.Add($okButton)

# Add a Cancel button
$cancelButton = New-Object System.Windows.Forms.Button
$cancelButton.Location = New-Object System.Drawing.Point(150, 220)
$cancelButton.Text = 'Cancel'
$cancelButton.DialogResult = [System.Windows.Forms.DialogResult]::Cancel
$form.CancelButton = $cancelButton
$form.Controls.Add($cancelButton)

# Show the form
$form.Topmost = $true
$form.Add_Shown({ $textBox.Select() })
$result = $form.ShowDialog()

# Handle user input
if ($result -eq [System.Windows.Forms.DialogResult]::OK) {
    $userInput = $textBox.Text
    $selectedOption = $radioButton1.Checked ? 'Option 1' : 'Option 2'
    $selectedItem = $comboBox.SelectedItem
    # Use $userInput, $selectedOption, and $selectedItem as needed
}

# Clean up
$form.Dispose()
