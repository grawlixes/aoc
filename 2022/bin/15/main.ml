open Core;;
include Lib;;
Printf.printf "\n";;
Printf.printf "Part 1:\n";;

(* Edit this with the correct day *)
let inp = 
    [Common.read_input "./bin/15/sample.txt";
     Common.read_input "./bin/15/input.txt"]
;;

let targets = [|10; 2000000|];;

let parse_read s =
    let reg = Str.regexp {|Sensor at x=\(.*\), y=\(.*\): closest beacon is at x=\(.*\), y=\(.*\)|} in
    let _ = Str.search_forward reg s 0 in
    let f i = int_of_string (Str.matched_group i s) in
    (f 1, f 2, f 3, f 4)
;;

(* Part 1 *)
List.iteri ~f:(fun index s ->
    (* Code goes here *)
    let t = targets.(index) in
    let visited = Hashtbl.create (module Int) in
    let beacons = Hashtbl.create (module Int) in 
    s
        |> String.split_on_chars ~on:['\n']
        |> List.filter ~f:(fun v -> String.length v > 0)
        |> List.iter ~f:(fun strin ->
            let (sx, sy, bx, by) = parse_read strin in
            if by = t then
                Hashtbl.set ~key:bx ~data:0 beacons;

            let dx = abs (sx - bx) in
            let dy = abs (sy - by) in
            let d = dx + dy in
            let d_target = abs (sy - t) in
            let stretch_x = d - d_target in

            if stretch_x >= 0 then begin 
                for i = (sx - stretch_x) to (sx + stretch_x) do
                    Hashtbl.set ~key:i ~data:0 visited;
                done;
            end;
        )
    ; 

    Hashtbl.iteri beacons ~f:(fun ~key ~data ->
        let _ = data in
        if Hashtbl.mem visited key then
            Hashtbl.remove visited key;
    );
    
    Printf.printf "%d\n" (Hashtbl.length visited);
    
    (* Separate output *)
    Printf.printf "-------\n";
) inp;;

Printf.printf "\nPart 2:\n";;

let distance (x1, y1) (x2, y2) =
    abs (x1 - x2) + (abs (y1 - y2))
;;

let lims = [|20; 4000000|];;

(* Part 2 
 * Somehow this works for the actual answer, but not the sample. lol 
 *)
List.iteri ~f:(fun index s ->
    (* Code goes here *)
    let lim = lims.(index) in
    let outer = ref [] in
    s
        |> String.split_on_chars ~on:['\n']
        |> List.filter ~f:(fun v -> String.length v > 0)
        |> List.iter ~f:(fun strin ->
            let (sx, sy, bx, by) = parse_read strin in
            let dx = abs (sx - bx) in
            let dy = abs (sy - by) in
            let d = dx + dy in
           
            let x1 = ref sx in
            let x2 = ref sy in
            if List.length !outer = 0 then begin
                for y = (sy - d - 1) to (sy + d + 1) do
                    outer := (!x1, y) :: !outer;
                    outer := (!x2, y) :: !outer;
                    x1 := !x1 + (if y < sy then (-1) else 1);
                    x2 := !x2 + (if y < sy then 1 else (-1));
                done;
            end else begin
                outer := List.filter ~f:(fun (x, y) ->
                    let dt = distance (x, y) (sx, sy) in
                    d < dt && (min x y >= 0) && (max x y <= lim) 
                ) !outer;
            end;
        )
    ; 

    List.iter ~f:(fun (x, y) ->
        Printf.printf "%d, %d\n" x y;
    ) !outer;
    
    (* Separate output *)
    Printf.printf "-------\n";
) inp;;

Printf.printf "\nPart 2:\n";;
