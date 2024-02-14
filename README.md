# calculator

A calculator application which include most mathematic functions and has some sounds when working and encountering errors

Sample interface : ("https://media.discordapp.net/attachments/1015464234664067122/1207294696389476372/image.png?ex=65df1fce&is=65ccaace&hm=d6e652a70b96c45f2e3910c98b17e7ae07914df7e37ff32b6c723fcabb143aa4&=&format=webp&quality=lossless&width=297&height=468")

# Normal mechanism

- After pressing buttons, there will be some sounds playing for normal working sounds.

# Top part

- The top part is for the history of your calculator.
- Below the history it is the main display of the calculator that shows typing stuffs and results.

# Purple part

- In the purple button group, they are numeric buttons that you can type the number and decimal point.
- Decimal point can type only once and program protects you from trying to type more than one by ignore your decimal point input.
- The ♪ button uses to play song randomly.

# Green part

- In the green button group, they are CLR, DEL and Select Function.
- DEL button deletes the last value, if the last value is "sqrt" then it will delete whole "sqrt".
- CLR button clear all history and current value
- Select Function works together with the Combobox. It will receive current value from Combobox and input to current equation on display.

# Function select

- Combobox contains some math functions for advanced calculation. Select one of them and press the Select Function button.

# Orange part

- In the orange button group, there are math operations and some constants.
- e and π buttons are math constant inputs.
- +,-,\*,/,^ buttons and mod are math operator inputs.
- = button is for start calculation.
- Parenthesis buttons are parenthesis inputs for the current equation.
- If the equation can be calculated successfully, it will be saved to history for user recallable and the success sound will be played.
- In contrast, if the equation fails, display text will turn to red and the error sound will be played.

# Pink part

- In pink button group, they are for estimating values.
- 2 Decimal button will give you 2 decimal place value.
- Normal button will give you 8 decimal place value.
- Science button will give you scientific number.
- If the estimation error, display text will be red and the error sound will be played.
- If the estimation success, success sound will be played.

UML class diagram : ("https://media.discordapp.net/attachments/1015464234664067122/1207294342973227038/hw01_1-24.jpg?ex=65df1f79&is=65ccaa79&hm=4deb19e653c2389b10a9d3e48d380b2304bf000a17def82c0c10164d623743a3&=&format=webp&width=362&height=467")
