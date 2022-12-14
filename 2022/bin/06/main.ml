open Core;;
include Lib;;

Printf.printf "\n";;
Printf.printf "Part 1:\n";;

(* Edit this with the correct day *)
let inp = 
    [Common.read_input "./bin/6/sample.txt";
     Common.read_input "./bin/6/input.txt"]
;;

(* Part 1 *)
List.iteri ~f:(fun _ s_untrimmed ->
    (* Code goes here *)
    let ct = Array.create ~len:26 0 in
    let s = String.strip s_untrimmed in
    let found = ref false in
    for i = 0 to (String.length s) - 1 do
        if not !found then (
            let ind = (Char.to_int (String.get s i)) - (Char.to_int 'a') in
            ct.(ind) <- ct.(ind) + 1;

            if ((i - 4) >= 0) then
                let ind_rem = (Char.to_int (String.get s (i-4))) - Char.to_int 'a' in
                ct.(ind_rem) <- (ct.(ind_rem) - 1);

            if (Array.fold ~f:(fun acc v -> acc && (v <= 1)) ~init:true ct) then (
                Printf.printf "%d\n" (i + 1);
                found := true;
            )
        )
    done;

    (* Separate output *)
    Printf.printf "-------\n";
) inp;;

Printf.printf "\nPart 2:\n";;

(* Part 2 *)
List.iteri ~f:(fun _ s_untrimmed ->
    (* Code goes here *)
    let ct = Array.create ~len:26 0 in
    let s = String.strip s_untrimmed in
    let found = ref false in
    for i = 0 to (String.length s) - 1 do
        if not !found then (
            let ind = (Char.to_int (String.get s i)) - (Char.to_int 'a') in
            ct.(ind) <- ct.(ind) + 1;

            if ((i - 14) >= 0) then
                let ind_rem = (Char.to_int (String.get s (i-14))) - Char.to_int 'a' in
                ct.(ind_rem) <- (ct.(ind_rem) - 1);

            if (Array.fold ~f:(fun acc v -> acc && (v <= 1)) ~init:true ct) then (
                Printf.printf "%d\n" (i + 1);
                found := true;
            )
        )
    done;

    (* Separate output *)
    Printf.printf "-------\n";
) inp;;
