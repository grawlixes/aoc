open Core;;
include Lib;;

Printf.printf "\n";;
Printf.printf "Part 1:\n";;

(* Edit this with the correct day *)
let inp = 
    [Common.read_input "./bin/04/sample.txt";
     Common.read_input "./bin/04/input.txt"]
;;

let to_pair s =
    let l = String.length s in
    let si = String.index_exn s '-' in
    
    (
        int_of_string (String.sub ~pos:0 ~len:si s),
        int_of_string (String.sub ~pos:(si+1) ~len:(l - si - 1) s)
    )
;;

let complete_overlap t1 t2 =
    let (x1,y1) = t1 in
    let (x2,y2) = t2 in 
    (x1 <= x2 && y2 <= y1) || (x2 <= x1 && y1 <= y2)
;;

let any_overlap t1 t2 =
    let (x1,y1) = t1 in
    let (x2,y2) = t2 in 
    not (
        y1 < x2 || y2 < x1
    )
;;

(* Part 1 *)
List.iter ~f:(fun s ->
    (* WRITE CODE HERE - input is "s" *)
    let ret = ref 0 in
    s
        |> String.split_on_chars ~on:['\n']
        |> List.filter ~f:(fun s -> String.length s > 0)
        |> List.iter ~f:(fun pairs ->
            let l = String.length pairs in
            let ci = String.index_exn pairs ',' in
            let pair1 =
                to_pair (String.sub ~pos:0 ~len:ci pairs) 
            in
            let pair2 = 
                to_pair (String.sub ~pos:(ci+1) ~len:(l - ci - 1) pairs)
            in
            
            if complete_overlap pair1 pair2 then
                ret := !ret + 1;
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
    s
        |> String.split_on_chars ~on:['\n']
        |> List.filter ~f:(fun s -> String.length s > 0)
        |> List.iter ~f:(fun pairs ->
            let l = String.length pairs in
            let ci = String.index_exn pairs ',' in
            let pair1 =
                to_pair (String.sub ~pos:0 ~len:ci pairs) 
            in
            let pair2 = 
                to_pair (String.sub ~pos:(ci+1) ~len:(l - ci - 1) pairs)
            in
            
            if any_overlap pair1 pair2 then
                ret := !ret + 1;
        )
    ;

    Printf.printf "%d\n" !ret;
    (* Separate sample and actual output *)
    Printf.printf "-----\n";
) inp;;
