# convert epoch to timestamp

- Reference:
  - https://unix.stackexchange.com/a/2993
  - https://www.epochconverter.com/ - this website shows the difference between 'milisecond' epoch and 'second' epoch

<table><tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
how can I convert "1751294737224" to "1751294737.224" using bash script?
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->
You can convert "1751294737224" to "1751294737.224" in a bash script using several methods. Here are a few common approaches:

-----

## Using `sed`

The `sed` command is excellent for text manipulation. This method works by inserting a decimal point three characters from the end of the string.

```bash
#!/bin/bash

number="1751294737224"
converted_number=$(echo "$number" | sed 's/.\{3\}$/.&/')
echo "$converted_number"
```

  * `s/`: This indicates the start of a substitution command.
  * `.\{3\}`: This matches any character (`.`) exactly three times (`\{3\}`).
  * `$`: This anchors the match to the end of the string.
  * `.&`: This is the replacement string. The `.` inserts a literal decimal point, and `&` represents the entire matched pattern (the last three characters). So, it effectively inserts a decimal before the last three characters.

-----

## Using `awk`

`awk` is another powerful text processing tool that can handle this.

```bash
#!/bin/bash

number="1751294737224"
converted_number=$(echo "$number" | awk '{printf "%.3f\n", $1/1000}')
echo "$converted_number"
```

  * `$1/1000`: This treats the input string as a number and divides it by 1000.
  * `printf "%.3f\n", ...`: This formats the result as a floating-point number with three decimal places.

-----

## Using Bash String Manipulation

Bash itself has capabilities for string manipulation, though it can be a bit more verbose for this specific task.

```bash
#!/bin/bash

number="1751294737224"
length=${#number}
# Get the part before the last three digits
before_decimal="${number:0:$((length-3))}"
# Get the last three digits
after_decimal="${number:$((length-3)):3}"
converted_number="${before_decimal}.${after_decimal}"
echo "$converted_number"
```

  * `${#number}`: Gets the length of the string.
  * `${number:OFFSET:LENGTH}`: This is bash's substring expansion.
      * `0:$((length-3))`: Extracts characters from the beginning up to three characters from the end.
      * `$((length-3)):3`: Extracts three characters starting from three characters before the end (i.e., the last three characters).

Each of these methods will successfully convert "1751294737224" to "1751294737.224". The best method depends on your preference and the specific context of your script. For simple string manipulation like this, `sed` is often considered very concise and readable.
</td></tr><tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
how to check string length using bash?
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->
You can check a string's length in Bash using the **`${#string}`** parameter expansion. This syntax directly provides the number of characters in the specified string variable.

-----

## Method

To use this, simply prepend a hash symbol (`#`) to the variable name within the curly braces.

```bash
#!/bin/bash

my_string="Hello, Bash!"
string_length=${#my_string}

echo "The string is: '$my_string'"
echo "Its length is: $string_length"

another_string=""
empty_string_length=${#another_string}

echo "The empty string's length is: $empty_string_length"
```

### Explanation

  * **`my_string="Hello, Bash!"`**: This line initializes a variable named `my_string` with the value "Hello, Bash\!".
  * **`string_length=${#my_string}`**: This is the core of the operation.
      * `#`: The hash symbol is the special character that tells Bash to return the length of the variable that follows.
      * `my_string`: This is the name of the variable whose length you want to measure.
      * `=${#my_string}`: The result (the length) is then assigned to the `string_length` variable.
  * **`echo "Its length is: $string_length"`**: This prints the calculated length to the console.

This method is efficient and is the standard way to determine string length directly within Bash scripts without needing external commands like `wc -c` or `awk`.
</td></tr></table>
