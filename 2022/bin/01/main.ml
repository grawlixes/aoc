open Core;;
include Lib;;

Printf.printf "\n";;
Printf.printf "Part 1:\n";;

(* Edit this with the correct day *)
let inp = 
    [Common.read_input "./bin/01/sample.txt";
     Common.read_input "./bin/01/input.txt"]
;;

(* Part 1 *)
List.iter ~f:(fun s ->
    (* WRITE CODE HERE - input is "s" *)
    let rec aux acc cur = function
        | [] -> acc
        | h :: t -> 
            if (String.length h > 0) then
                aux acc (cur + int_of_string h) t
            else
                aux (max acc cur) 0 t
    in
    s
        |> String.split_on_chars ~on:['\n']
        |> aux 0 0
        |> Printf.printf "%d\n" 
    ;
    (* Separate sample and actual output *)
    Printf.printf "-----\n";
) inp;;

Printf.printf "\nPart 2:\n";;

let rec push acc x =
    if acc.(0) < x then
        let n = acc.(0) in
        Array.set acc 0 x;
        push acc n;
    else if acc.(1) < x then
        let n = acc.(1) in
        Array.set acc 1 x;
        push acc n;
    else if acc.(2) < x then
        Array.set acc 2 x;
;;

(* Part 2 *)
List.iter ~f:(fun s ->
    (* WRITE CODE HERE - input is "s" *)
    let rec aux acc cur = function
        | [] -> acc
        | h :: t -> 
            if (String.length h > 0) then
                aux acc (cur + int_of_string h) t
            else (
                push acc cur;
                aux acc 0 t
            )
    in
    s
        |> String.split_on_chars ~on:['\n']
        |> aux [|0; 0; 0|] 0
        |> Array.sum (module Int) ~f:Fn.id
        |> Printf.printf "%d\n" 
    ;
    (* Separate sample and actual output *)
    Printf.printf "-----\n";
) inp;;
