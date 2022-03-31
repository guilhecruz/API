<?php

if(isset($_POST['email']) and isset($_POST['senha'])){
$url = "http://localhost:8000/login";

$curl = curl_init($url);
curl_setopt($curl, CURLOPT_URL, $url);
curl_setopt($curl, CURLOPT_POST, true);
curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);

$headers = array(
   "Content-Type: application/json",
);
curl_setopt($curl, CURLOPT_HTTPHEADER, $headers);

$data = json_encode(array(
  "email"=> $_POST['email'],
  "senha" = > $_POST['senha']
));


curl_setopt($curl, CURLOPT_POSTFIELDS, $data);
}
else{
    echo 'Informe um email e uma senha'
}
//for debug only!
curl_setopt($curl, CURLOPT_SSL_VERIFYHOST, false);
curl_setopt($curl, CURLOPT_SSL_VERIFYPEER, false);

$resp = curl_exec($curl);
curl_close($curl);
var_dump($resp);

?>