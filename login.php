<?php
$servername = "localhost";
$username = "root";
$password = "rajkumar@123@";
$dbname = "parahelp101";


// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $user = $_POST['username'];
    $pass = $_POST['password'];

    // Prepare the statement to fetch the user
    $stmt = $conn->prepare("SELECT * FROM users WHERE username = ?");
    $stmt->bind_param("s", $user);
    $stmt->execute();
    $result = $stmt->get_result();

    if ($result->num_rows > 0) {
        $row = $result->fetch_assoc();
        
        // Verify the password
        if (password_verify($pass, $row['password'])) {
            echo "<script>alert('Login successful!'); window.location.href='p.html';</script>";
        } else {
            echo "<script>alert('Invalid username or password.'); window.location.href='login.html';</script>";
        }
    } else {
        echo "<script>alert('Invalid username or password.'); window.location.href='login.html';</script>";
    }

    $stmt->close();
}
$conn->close();
?>

















































