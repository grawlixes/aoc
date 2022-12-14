open Core;;
include Lib;;

Printf.printf "\n";;
Printf.printf "Part 1:\n";;

(* Edit this with the correct day *)
let inp = 
    [Common.read_input "./bin/2/sample.txt";
     Common.read_input "./bin/2/input.txt"]
;;

let score c =
    let res =
        (Char.to_int c) - (Char.to_int 'X')
    in
    if (res >= 0) then res
    else 
        (Char.to_int c) - (Char.to_int 'A')
;;

let wins foe me =
    (score foe + 1) mod 3 = score me
;;

(* Part 1 *)
List.iter ~f:(fun s ->
    (* WRITE CODE HERE - input is "s" *)
    s
        |> String.split_on_chars ~on:['\n']
        |> List.sum (module Int) ~f:(fun s ->
            if String.length s = 0 then 
                0
            else
                let foe = String.get s 0 in
                let me = String.get s 2 in
                
                (score me) + 1 + (
                    if (wins foe me) then 6
                    else if (score foe = score me) then 3
                    else 0
                )
        )
        |> Printf.printf "%d\n"
    ;
    (* Separate sample and actual output *)
    Printf.printf "-----\n";
) inp;;

Printf.printf "\nPart 2:\n";;

(* Part 2 *)
List.iter ~f:(fun s ->
    (* WRITE CODE HERE - input is "s" *)
    s
        |> String.split_on_chars ~on:['\n']
        |> List.sum (module Int) ~f:(fun s ->
            if String.length s = 0 then 
                0
            else
                let fs = score (String.get s 0) in
                let rs = score (String.get s 2) in

                (* this is where I learned that ocaml modulo for negatives is stupid. 
                 * -1 mod 3 = -1 :/ 
                 *)                
                if rs = 0 then
                    (if fs > 0 then (fs - 1) else 2) 
                        + 1 + 0
                else if rs = 1 then
                    fs + 1 + 3
                else
                    ((fs + 1) mod 3) + 1 + 6
        )
        |> Printf.printf "%d\n"
    ;
    (* Separate sample and actual output *)
    Printf.printf "-----\n";
) inp;;
