open Core;;
include Lib;;
Printf.printf "\n";;
Printf.printf "Part 1:\n";;

(* Edit this with the correct day *)
let inp = 
    [Common.read_input "./bin/14/sample.txt";
     Common.read_input "./bin/14/input.txt"]
;;

let extract s =
    let comma = String.index_exn s ',' in
    let sl = String.length s - comma - 1 in
    (int_of_string (String.sub ~pos:0 ~len:comma s),
     int_of_string (String.sub ~pos:(comma+1) ~len:sl s)
    )
;;

let comp x y = match x with
    | z when z = y -> 0
    | z when z < y -> 1
    | _ -> (-1)
;;

let valid grid cutoff =
    let x = ref 500 in
    let y = ref 0 in
    let placed = ref false in
    while (not !placed) && (!y <> cutoff) do
        if grid.(!x).(!y+1) = 0 then begin
            y := !y + 1;
        end else if grid.(!x-1).(!y+1) = 0 then begin
            x := !x - 1;
            y := !y + 1;
        end else if grid.(!x+1).(!y+1) = 0 then begin
            x := !x + 1;
            y := !y + 1;
        end else begin
            placed := true;
        end;
    done;

    if !placed then 
        grid.(!x).(!y) <- 2;
    
    !placed
;;

(* Part 1 *)
List.iter ~f:(fun s ->
    (* Code goes here *)
    let grid = Array.make_matrix ~dimx:1000 ~dimy:200 0 in
    let cutoff = ref 0 in
    s
        |> String.split_on_chars ~on:['\n']
        |> List.iter ~f:(fun line ->
            let px = ref 0 in
            let py = ref 0 in
            line
                |> Str.split (Str.regexp " -> ")
                |> List.iter ~f:(fun cs ->
                    let (x, y) = extract cs in
                    if !px <> 0 || !py <> 0 then ( 
                        let dx = comp !px x in
                        let dy = comp !py y in
                        while !px <> x || !py <> y do
                            grid.(!px).(!py) <- 1;
                            px := !px + dx;
                            py := !py + dy;
                            cutoff := max !cutoff !py;
                        done;
                        grid.(!px).(!py) <- 1;
                    ) else (
                        px := x;
                        py := y;
                    )
                );
        );

    let ret = ref 0 in
    while valid grid !cutoff do
        ret := !ret + 1;
    done;

    Printf.printf "%d\n" !ret;

    (* Separate output *)
    Printf.printf "-------\n";
) inp;;

Printf.printf "\nPart 2:\n";;
(* Part 2 *)
List.iter ~f:(fun s ->
    (* Code goes here *)
    let grid = Array.make_matrix ~dimx:1000 ~dimy:200 0 in
    let cutoff = ref 0 in
    s
        |> String.split_on_chars ~on:['\n']
        |> List.iter ~f:(fun line ->
            let px = ref 0 in
            let py = ref 0 in
            line
                |> Str.split (Str.regexp " -> ")
                |> List.iter ~f:(fun cs ->
                    let (x, y) = extract cs in
                    if !px <> 0 || !py <> 0 then ( 
                        let dx = comp !px x in
                        let dy = comp !py y in
                        while !px <> x || !py <> y do
                            grid.(!px+0).(!py) <- 1;
                            px := !px + dx;
                            py := !py + dy;
                            cutoff := max !cutoff !py;
                        done;
                        grid.(!px+0).(!py) <- 1;
                    ) else (
                        px := x;
                        py := y;
                    )
                );
        )
    ;

    cutoff := !cutoff + 2;
    Common.range 0 1000 1
        |> List.iter ~f:(fun i -> 
            grid.(i).(!cutoff) <- 1;
        )
    ; 

    let ret = ref 0 in
    while grid.(500).(0) = 0 && (valid grid !cutoff) do
        ret := !ret + 1;
    done;

    Printf.printf "%d\n" !ret;

    (* Separate output *)
    Printf.printf "-------\n";
) inp;;
