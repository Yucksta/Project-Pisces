<?php
    $counter = 92;
    $counter *= 2;
    $result = [];
    while ($counter > 0) {
        $remaining = $counter % 2;
        $result[sizeof($result)] = $remaining;
        $counter = floor($counter / 2);
    };
    for ($i = sizeof($result) - 1; $i > 0; $i--) {
        echo $result[$i];
    };
?>