function Show-MyPowerShellForm {
    param (
        [ref]$userInput,
        [ref]$selectedOption,
        [ref]$selectedItem
    )

    # Rest of the form creation code (same as before)

    # Show the form
    $form.Topmost = $true
    $form.Add_Shown({ $textBox.Select() })
    $result = $form.ShowDialog()

    # Handle user input
    if ($result -eq [System.Windows.Forms.DialogResult]::OK) {
        $userInput.Value = $textBox.Text
        $selectedOption.Value = if ($radioButton1.Checked) { 'Option 1' } else { 'Option 2' }
        $selectedItem.Value = $comboBox.SelectedItem
    }

    # Clean up
    $form.Dispose()
}

# Example usage:
$myUserInput = $null
$mySelectedOption = $null
$mySelectedItem = $null

Show-MyPowerShellForm ([ref]$myUserInput) ([ref]$mySelectedOption) ([ref]$mySelectedItem)

# Now you can access $myUserInput, $mySelectedOption, and $mySelectedItem globally.
