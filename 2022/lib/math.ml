open Core;;

(* Returns x^a *)
let rec pow a = function
  | 0 -> 1
  | 1 -> a
  | n ->
    let b = pow a (n / 2) in
    b * b * (if n mod 2 = 0 then 1 else a)
;;

(* Greatest common divisor of A and B *)
let rec gcd a b =
    if (b = 0) then a
    else gcd b (a mod b)
;;

(* Least common multiple of A and B *)
let lcm a b = (a * b) / (gcd a b);;

(* Get divisors of l *)
let divisors l =
    let rec aux acc = function
        | 0 -> acc
        | x  ->
            if (l mod x = 0) then
                if (x = (l / x)) then
                    aux (x :: acc) (x - 1)
                else
                    aux (x :: (l / x) :: acc) (x - 1)
            else
                aux acc (x - 1)
    in
     let limit = (Int.to_float l)
    in
     aux [] ((Int.of_float (Float.sqrt limit)))
;;

(* Generates all prime numbers up to n with sieve *)
let primes_up_to n =
    let primes = Array.create ~len:(n+1) true in
    let rec mark p i =
        if (i <= n) then (
            primes.(i) <- false;
            mark p (i + p)
        )
    in
    primes.(0) <- false;
    primes.(1) <- false;
    for i = 2 to n do
        if (primes.(i)) then
            mark i (2*i);
    done;
    primes
;;
