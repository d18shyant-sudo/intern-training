# SQL Agent Prompt Change Log

This changelog records each prompt version, the user input, expected output, actual model output, the change made, and the result.

---

## Version 1

### Prompt Used

```text
(set-up)>>> you are sql agent and convert all nautral language to sql commands

Sure, I can help with that! Please provide a natural language query or statement, and I'll convert it to the corresponding SQL command. For example:

- "Show me all employees in the sales department."
- "Find the total sales for each product category."
- "Update the salary of all employees who joined after 2015."

Feel free to provide your request, and I'll translate it into SQL!
```

### User Input

```text
show the last sold product in last month
```

### Expected Output

```text
Only the SQL command corresponding to the user's natural-language request.
```

### Actual Output

```text
To show the last sold product in the last month, you'll need to have a table that tracks sales and includes the date of each sale. Let's assume you have a table named `Sales` with the following columns:

- `product_id`: The ID of the product.
- `sale_date`: The date of the sale.

Here's the SQL query to get the last sold product in the last month:

```sql
SELECT product_id, sale_date
FROM Sales
WHERE sale_date >= DATEADD(month, -1, GETDATE())
ORDER BY sale_date DESC
OFFSET 0 ROWS
FETCH NEXT 1 ROW ONLY;
```

Explanation:
- `DATEADD(month, -1, GETDATE())` calculates the date one month before the current date.
- `WHERE sale_date >= DATEADD(month, -1, GETDATE())` filters the sales that occurred in the last month.
- `ORDER BY sale_date DESC` sorts the sales in descending order by date, so the most recent sale comes first.
- `OFFSET 0 ROWS FETCH NEXT 1 ROW ONLY` ensures that only the first (most recent) row is returned.

If your SQL dialect does not support `OFFSET` and `FETCH`, you can use a different approach:

```sql
SELECT product_id, sale_date
FROM Sales
WHERE sale_date >= DATEADD(month, -1, GETDATE())
ORDER BY sale_date DESC
LIMIT 1;
```

This will achieve the same result in SQL Server, but if you're using a different SQL dialect, please let me know so I can adjust the query accordingly.
```

### What Changed

Initial SQL-agent prompt was created.

### Result

**FAIL**

### Problem

The model generated explanations, assumptions, Markdown code fences, and multiple SQL alternatives instead of returning only SQL.

---

## Version 2

### Prompt Used

```text
(set-up)>>> you are sql agent and convert all nautral language to sql commands

(1)>>> show the last sold product in last month

(2)>>> show the last sold product in last month.no dessciption only the sql cmds
```

### User Input

```text
show the last sold product in last month.no dessciption only the sql cmds
```

### Expected Output

```text
Only the SQL command.
No explanation or additional text.
```

### Actual Output

```text
Sure, here is the SQL command to show the last sold product in the last month:

```sql
SELECT product_id, sale_date
FROM Sales
WHERE sale_date >= DATEADD(month, -1, GETDATE())
ORDER BY sale_date DESC
LIMIT 1;
```

This query will return the `product_id` and `sale_date` of the last sold product in the last month.
```

### What Changed

Added the instruction:

```text
no dessciption only the sql cmds
```

### Result

**FAIL**

### Problem

The model still generated an introduction, conclusion, and Markdown code fences.

---

## Version 3

### Prompt Used

```text
(set-up)>>> you are sql agent and convert all nautral language to sql commands

(1)>>> show the last sold product in last month

(2)>>> show the last sold product in last month.no dessciption only the sql cmds

(3)>>> show the last sold product in last month.no sentence on inroduction,explanation and conclusin just give the raw sql
```

### User Input

```text
show the last sold product in last month.no sentence on inroduction,explanation and conclusin just give the raw sql
```

### Expected Output

```text
Only raw SQL.
No introduction.
No explanation.
No conclusion.
No Markdown code fence.
```

### Actual Output

```text
```sql
SELECT product_id, sale_date
FROM Sales
WHERE sale_date >= DATEADD(month, -1, GETDATE())
ORDER BY sale_date DESC
LIMIT 1;
```
```

### What Changed

Added an explicit instruction to remove sentences from the introduction, explanation, and conclusion and return raw SQL.

### Result

**FAIL**

### Problem

The model removed the surrounding prose but still returned the SQL inside a Markdown code fence.

---

## Version 4

### Prompt Used

```text
(set-up)>>> you are sql agent and convert all nautral language to sql commands

(1)>>> show the last sold product in last month

(2)>>> show the last sold product in last month.no dessciption only the sql cmds

(3)>>> show the last sold product in last month.no sentence on inroduction,explanation and conclusin just give the raw sql

(4)>>> show the last sold product in last month.no sentence on inroduction,explanation and conclusin just give the raw sql commands that begins with capital letter and with ;
```

### User Input

```text
show the last sold product in last month.no sentence on inroduction,explanation and conclusin just give the raw sql commands that begins with capital letter and with ;
```

### Expected Output

```text
SQL command beginning with a capitalized SQL keyword and ending with a semicolon.
No Markdown code fences.
No additional text.
```

### Actual Output

```text
```sql
SELECT product_id, sale_date
FROM Sales
WHERE sale_date >= DATEADD(month, -1, GETDATE())
ORDER BY sale_date DESC
LIMIT 1;
```
```

### What Changed

Added the requirements that:

- The SQL command begins with a capital letter.
- The SQL command ends with `;`.

### Result

**FAIL**

### Problem

The model followed the SQL capitalization and semicolon requirements but continued to wrap the output in Markdown code fences.

---

## Version 5

### Prompt Used

```text
(set-up)>>> you are sql agent and convert all nautral language to sql commands

(1)>>> show the last sold product in last month

(2)>>> show the last sold product in last month.no dessciption only the sql cmds

(3)>>> show the last sold product in last month.no sentence on inroduction,explanation and conclusin just give the raw sql

(4)>>> show the last sold product in last month.no sentence on inroduction,explanation and conclusin just give the raw sql commands that begins with capital letter and with ;

(5)>>> show the last sold product in last month.no sentence on inroduction,explanation and conclusin just give the raw sql commands that begins with capital letter and with ; and it not start with ```sql and not end with ``` remove and give only the except that
```

### User Input

```text
show the last sold product in last month.no sentence on inroduction,explanation and conclusin just give the raw sql commands that begins with capital letter and with ; and it not start with ```sql and not end with ``` remove and give only the except that
```

### Expected Output

```text
SELECT Product_ID, Sale_Date
FROM Sales
WHERE Sale_Date >= DATEADD(month, -1, GETDATE())
ORDER BY Sale_Date DESC
LIMIT 1;
```

### Actual Output

```text
SELECT Product_ID, Sale_Date
FROM Sales
WHERE Sale_Date >= DATEADD(month, -1, GETDATE())
ORDER BY Sale_Date DESC
LIMIT 1;
```

### What Changed

Added an explicit requirement that the response:

- Must not start with ` ```sql `.
- Must not end with ` ``` `.
- Must contain only the SQL output.
- Must preserve the previously established capitalization and semicolon requirements.

### Result

**PASS**

### Problem Solved

The model finally returned only the raw SQL without:

- Introduction
- Explanation
- Conclusion
- Markdown code fences
- Additional text

---

## Summary

| Version | Main Change | Result |
|---|---|---|
| Version 1 | Basic natural-language-to-SQL instruction | FAIL |
| Version 2 | Added "no description only SQL commands" | FAIL |
| Version 3 | Explicitly removed introduction, explanation, and conclusion | FAIL |
| Version 4 | Added capitalization and semicolon requirements | FAIL |
| Version 5 | Explicitly prohibited Markdown SQL fences and extra output | PASS |

## Overall Observation

The prompt evolved from a general instruction into an explicit output-format specification.

The main failure across the first four versions was that the model interpreted "only SQL" semantically but continued to use Markdown formatting and conversational text. Version 5 explicitly constrained the output boundaries, which resulted in the desired raw SQL output.
