open Core;;
include Lib;;

Printf.printf "\n";;
Printf.printf "Part 1:\n";;

(* Edit this with the correct day *)
let inp = 
    [Common.read_input "./bin/3/sample.txt";
     Common.read_input "./bin/3/input.txt"]
;;

let priority ch =
    if (Char.equal ch (Char.lowercase ch)) then
        (Char.to_int ch) - (Char.to_int 'a')
    else
        (Char.to_int ch) - (Char.to_int 'A') + 26
;;

let lowers = "abcdefghijklmnopqrstuvwxyz";;
let uppers = String.uppercase lowers;;

(* Part 1 *)
List.iter ~f:(fun s ->
    (* WRITE CODE HERE - input is "s" *)
    let ret = ref 0 in
    s
        |> String.split_on_chars ~on:['\n']
        |> List.filter ~f:(fun s -> String.length s > 0)
        |> List.iter ~f:(fun s ->
            let in_both = Array.create ~len:52 true in
            let half = (String.length s) / 2 in
            let left = String.sub ~pos:0 ~len:half s in
            let right = String.sub ~pos:half ~len:half s in
            
            (lowers ^ uppers)
                |> String.iter ~f:(fun ch ->
                    if ((not (String.contains left ch)) || 
                        (not (String.contains right ch))) then
                        Array.set in_both (priority ch) false;
                );

            in_both
                |> Array.iteri ~f:(fun i b ->
                    if b then 
                        ret := !ret + (i + 1);
                )
            ;
        )
    ;

    Printf.printf "%d\n" !ret;
    
    (* Separate sample and actual output *)
    Printf.printf "-----\n";
) inp;;

Printf.printf "\nPart 2:\n";;
List.iter ~f:(fun s ->
    (* WRITE CODE HERE - input is "s" *)
    let ret = ref 0 in
    let a = String.split_on_chars ~on:['\n'] s
        |> Array.of_list
    in
    (Common.range 0 (Array.length a) 3)
        |> List.iter ~f:(fun i ->
            let in_all = Array.create ~len:52 true in
            for ind = i to (i+2) do
                let s = Array.get a ind in 
                (lowers ^ uppers)
                    |> String.iter ~f:(fun ch ->
                        if (not (String.contains s ch)) then
                            Array.set in_all (priority ch) false;
                    )
                ;
            done;

            in_all
                |> Array.iteri ~f:(fun i b ->
                    if b then 
                        ret := !ret + (i + 1);
                )
            ;
        )
    ;

    Printf.printf "%d\n" !ret;
    
    (* Separate sample and actual output *)
    Printf.printf "-----\n";
) inp;;
