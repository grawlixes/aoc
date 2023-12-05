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
    s
        |> String.split_on_chars ~on:['\n']
        |> (fun s2 -> Printf.printf s2 + ", ";)
    ;
) inp;;
