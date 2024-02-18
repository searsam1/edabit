function isNarcissistic($num) {
	$res = [];
	$len = strlen($num);
	$arr = str_split($num);
	foreach($arr as $v){
		array_push($res, pow($v, $len));
	}
	return array_sum($res) === $num;
}