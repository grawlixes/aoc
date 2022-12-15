open Core;;
include Lib;;

Printf.printf "\n";;
Printf.printf "Part 1:\n";;

(* Edit this with the correct day *)
let inp = 
    [Common.read_input "./bin/08/sample.txt";
     Common.read_input "./bin/08/input.txt"]
;;

let on_edge grid i j =
    let n = Array.length grid in
    let m = Array.length grid.(0) in
    (i = 0 || j = 0 || i = (n-1) || j = (m-1))
;;

let rec max_on_line grid i j di dj = 
    let n = Array.length grid in
    let m = Array.length grid.(0) in
    if (i < 0 || j < 0 || i = n || j = m) then
        0
    else
        max grid.(i).(j) (max_on_line grid (i+di) (j+dj) di dj)
;;

(* Part 1 *)
List.iteri ~f:(fun _ s ->
    (* Code goes here *)
    let ret = ref 0 in
    let grid = s
        |> String.split_on_chars ~on:['\n']
        |> List.filter ~f:(fun s -> String.length s > 0)
        |> List.map ~f:(fun s ->
            Array.init (String.length s) ~f:(fun ind -> Common.char_to_int (s.[ind]))
        )
        |> Array.of_list
    in
    Array.iteri ~f:(fun i row ->
        Array.iteri ~f:(fun j cell ->
            let maxes =
                [
                 max_on_line grid (i-1) j (-1) 0;
                 max_on_line grid i (j-1) 0 (-1);
                 max_on_line grid i (j+1) 0 ( 1);
                 max_on_line grid (i+1) j ( 1) 0
                ] 
            in
            if (on_edge grid i j) || (Common.min maxes) < cell then
                ret := !ret + 1;
        ) row;
    ) grid;
    
    Printf.printf "%d\n" !ret;

    (* Separate output *)
    Printf.printf "-------\n";
) inp;;

Printf.printf "\nPart 2:\n";;

let rec trees_visible_on_line grid og i j di dj =
    let n = Array.length grid in
    let m = Array.length grid.(0) in
    if (i < 0 || j < 0 || i = n || j = m) then
        0
    else
        let cell = grid.(i).(j) in
        if (og <= cell) then
            1
        else
            (trees_visible_on_line grid og (i+di) (j+dj) di dj) + 1
;;

(* Part 2 *)
List.iteri ~f:(fun _ s ->
    (* Code goes here *)
    let ret = ref 0 in
    let grid = s
        |> String.split_on_chars ~on:['\n']
        |> List.filter ~f:(fun s -> String.length s > 0)
        |> List.map ~f:(fun s ->
            Array.init (String.length s) ~f:(fun ind -> Common.char_to_int (s.[ind]))
        )
        |> Array.of_list
    in
    Array.iteri ~f:(fun i row ->
        Array.iteri ~f:(fun j cell ->
            let maxes =
                [
                 trees_visible_on_line grid cell (i-1) j (-1) 0;
                 trees_visible_on_line grid cell i (j-1) 0 (-1);
                 trees_visible_on_line grid cell i (j+1) 0 ( 1);
                 trees_visible_on_line grid cell (i+1) j ( 1) 0
                ] 
            in
            ret := max !ret (
                List.fold_left ~f:(fun acc x -> acc*x) ~init:1 maxes
            );
        ) row;
    ) grid;
    
    Printf.printf "%d\n" !ret;

    (* Separate output *)
    Printf.printf "-------\n";
) inp;;
