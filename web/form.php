<!DOCTYPE HTML>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" 
content="width=device-width,
initial-scale=1.0">
<title>Form Sweet Form</title>
</head>

<body align ="center" style=
"color:black;background-color:white;">

<form method="get" autocomplete="off"
align="center" action="/form.php">

<input size="30" 
type="text" name="title"
placeholder="Place your title here"/>

<input rows="5" 
type="textarea" name="content"
placeholder="place your content here"/>


</form>

<br/><br/>

<a href="index.php"
style="text-decoration:none;">
Go Home</a>
</body>
</html>

<?php
if( isset($_GET['title']) )
{
     echo "<br/><br/>".$_GET['title']
."<br/><br/><br/>".$_GET['content'];
}
?>
