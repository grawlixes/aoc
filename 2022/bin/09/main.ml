open Core;;
include Lib;;

Printf.printf "\n";;
Printf.printf "Part 1:\n";;

module Pair = struct
    type t = int * int [@@deriving compare, sexp_of]
end;;

module IntPair = struct 
    include Pair
    include Base.Comparator.Make(Pair)
    let hash = Hashtbl.hash
end;;

(* Edit this with the correct day *)
let inp = 
    [Common.read_input "./bin/9/sample.txt";
     Common.read_input "./bin/9/input.txt"]
;;

let d_map c = match c with
    | 'U' -> (-1, 0)
    | 'R' -> (0, 1)
    | 'D' -> (1, 0)
    | 'L' -> (0, -1)
    | _ -> (0, 0)
;;

let get_instruction s =
    let l = String.length s in
    let ct = int_of_string (String.sub ~pos:2 ~len:(l - 2) s) in
    (s.[0], ct)
;;

let directions_same =
    [((-1), 0); (0, (-1)); (0, 1); (1, 0)]
;;

let directions_different = 
    [(-1, -1); (-1, 1); (1, -1); (1, 1)]
;;

let are_neighbors hi hj ti tj sp =
    let diff = (abs (hi - ti)) + (abs (hj - tj)) in
    if sp then 
        Printf.printf "Trying %d %d %d %d: %d\n" hi hj ti tj diff;
    if (hi = ti) || (hj = tj) then
        diff <= 1
    else
        diff <= 2
;;

(* Part 1 *)
List.iteri ~f:(fun _ s ->
    (* Code goes here *)
    let seen = Hashtbl.create (module IntPair) in
    let hi = ref 0 in
    let hj = ref 0 in
    let ti = ref 0 in
    let tj = ref 0 in 
    s
        |> String.split_on_chars ~on:['\n']
        |> List.filter ~f:(fun s -> String.length s > 0)
        |> List.iter ~f:(fun s ->
            let (d,ct) = get_instruction s in
            let (di,dj) = d_map d in
            for _ = 1 to ct do
                hi := !hi + di;
                hj := !hj + dj;
                if not (are_neighbors !hi !hj !ti !tj false) then (
                    let directions =
                        if (!hi = !ti) || (!hj = !tj) then
                            directions_same
                        else
                            directions_different
                    in
                    let (nti, ntj) = directions
                        |> List.find_exn ~f:(fun (dti, dtj) ->
                            let (tti, ttj) = (!ti + dti, !tj + dtj) in
                            are_neighbors !hi !hj tti ttj false
                        )
                    in
                    ti := !ti + nti;
                    tj := !tj + ntj; 
                );
               
                Hashtbl.set ~key:(!ti, !tj) ~data:0 seen;
            done;
        )
    ;
    
    Printf.printf "%d\n" (Hashtbl.length seen);

    (* Separate output *)
    Printf.printf "-------\n";
) inp;;

Printf.printf "\nPart 2:\n";;
(* Part 2 *)
List.iteri ~f:(fun _ s ->
    (* Code goes here *)
    let seen = Hashtbl.create (module IntPair) in 
    let indices = Array.create ~len:10 (0,0) in
    s
        |> String.split_on_chars ~on:['\n']
        |> List.filter ~f:(fun s -> String.length s > 0)
        |> List.iter ~f:(fun s ->
            let (d,ct) = get_instruction s in
            let (di,dj) = d_map d in
            for _ = 1 to ct do
                let (oi, oj) = indices.(0) in
                indices.(0) <- (oi+di, oj+dj);
                for ind = 1 to 9 do
                    let (hi, hj) = indices.(ind-1) in
                    let (ti, tj) = indices.(ind) in
                    if not (are_neighbors hi hj ti tj false) then (
                        let directions =
                            if (hi = ti) || (hj = tj) then
                                directions_same
                            else
                                directions_different
                        in
                        let (nti, ntj) = directions
                            |> List.find_exn ~f:(fun (dti, dtj) ->
                                let (tti, ttj) = (ti + dti, tj + dtj) in
                                are_neighbors hi hj tti ttj false
                            )
                        in
                        indices.(ind) <- (ti + nti, tj + ntj);
                    );
                done;

                Hashtbl.set ~key:indices.(9) ~data:0 seen;
            done;
        )
    ;
    
    Printf.printf "%d\n" (Hashtbl.length seen);

    (* Separate output *)
    Printf.printf "-------\n";
) inp;;

Printf.printf "\nPart 2:\n";;
