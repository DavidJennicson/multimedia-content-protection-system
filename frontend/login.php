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
		
$sql = "SELECT  * FROM accounts WHERE useremail  = '".$usersignupemail."' AND username  ='".$usersignupname."'";
$result = $conn->query($sql);

if ($result->num_rows == 0)
{
		$stmt = $conn->prepare("insert into accounts(username,useremail,userpassword) values(?, ?, ?)");
		$stmt->bind_param("sss", $usersignupname,$usersignupemail,$usersignuppassword);
		$execval = $stmt->execute();
		echo $execval;
		echo "Registration successfully";
		$stmt->close();
		$conn->close();
}
else{
	echo"Account already exists!";
}	

}

?>