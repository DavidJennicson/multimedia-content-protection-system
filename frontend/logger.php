
<?php

	$usersignupname = $_POST['usersignupname'];
	$usersignupemail= $_POST['usersignupemail'];
    $usersignuppassword = $_POST['usersignuppassword'];
	// Database connection
	$conn = new mysqli('localhost','root','','accounts');
	if($conn->connect_error){
		echo "$conn->connect_error";
		die("Connection Failed : ". $conn->connect_error);
	} else {
		
$sql = "SELECT  * FROM accounts WHERE useremail  = '".$usersignupemail."' AND userpassword='".$usersignuppassword."'";
$result = $conn->query($sql);

if ($result->num_rows == 0)
{
    if($count == 1) {
        
        header("location: welcome.php");
     }else {
        $error = "Your Login Name or Password is invalid";
     }
}
else{
	echo"Account already exists!";
}	

}

?>
