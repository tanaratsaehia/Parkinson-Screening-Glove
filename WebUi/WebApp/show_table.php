<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Table</title>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js" integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN" crossorigin="anonymous"></script>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
</head>
<body>
    <div class="container">
        <?php
            $username = $_GET['name'];
            $time = $_GET['datetime'];
        ?>
        <div class="h4 text-center alert alert-primary mb-2 mt-4" role="alert">Table</div><br>
        <div class="h5"><?=$username?> <small class="text-muted"><?=$time?></small></div><br>
        
        <table class="table table-striped">
            <tr>
                <th>No</th>
                <th>Data</th>
                <th>PredictValue</th>
            </tr>
            <?php
                include 'condb.php';
                $table = $_GET['table'];
                $sql = "SELECT * FROM $table";
                $result = mysqli_query($conn, $sql);
                $row_count = 1;
                while ($row = mysqli_fetch_array($result)){
            ?>
            <tr>
                <td><?=$row_count?></td>
                <td><?=$row['data']?></td>
                <td><?=$row['predict_value']?></td>
            </tr>
            <?php
                $row_count += 1;
                }
                mysqli_close($conn);
            ?>
        </table>
    </div>
</body>
</html>