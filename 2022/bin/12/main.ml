open Core;;
include Lib;;

Printf.printf "\n";;
Printf.printf "Part 1:\n";;

(* Edit this with the correct day *)
let inp = 
    [Common.read_input "./bin/12/sample.txt";
     Common.read_input "./bin/12/input.txt"]
;;

let char_index ch = 
    if Char.equal ch (Char.lowercase ch) then
        (Char.to_int ch) - (Char.to_int 'a')
    else if Char.equal ch 'S' then
        0
    else
        25
;;

let find_cells grid n m ch =
    Common.generate_pairs 0 0 n m 1
        |> List.filter ~f:(fun (i, j) ->
            Char.equal grid.(i).(j) ch
        )
;;

let neighbors grid i j =
    let (n, m) = (Array.length grid, Array.length grid.(0)) in
    let cell = grid.(i).(j) in
    [(i-1, j); (i, j-1); (i, j+1); (i+1, j)]
        |> List.filter ~f:(fun (i2, j2) ->
            min i2 j2 >= 0 &&
            i2 < n &&
            j2 < m
        )
        |> List.filter ~f:(fun (i2, j2) ->
            let move_cell = grid.(i2).(j2) in
            (char_index move_cell) <= (char_index cell) + 1
        )
;;

(* Part 1 *)
List.iter ~f:(fun s ->
    (* Code goes here *)
    let grid = s
        |> String.split_on_chars ~on:['\n']
        |> List.filter_map ~f:(fun s -> 
            let l = String.length s in
            if l = 0 then
                None
            else
                Some (Array.init l ~f:(fun i ->
                    s.[i]
                ))
        )
        |> Array.of_list
    in
    let (n, m) = (Array.length grid, Array.length grid.(0)) in
    let (si, sj) = List.nth_exn (find_cells grid n m 'S') 0 in
    let seen = Array.make_matrix ~dimx:n ~dimy:m false in
    let q = Queue.create () in
    Queue.enqueue q (si, sj, 0);
    while Queue.length q > 0 do
        let (i, j, ct) = Queue.dequeue_exn q in
        if not (seen.(i).(j)) then begin
            seen.(i).(j) <- true;
            if Char.equal grid.(i).(j) 'E' then begin
                Printf.printf "%d\n" ct;
            end;
            
            (neighbors grid i j)
                |> List.iter ~f:(fun (i2, j2) ->
                    Queue.enqueue q (i2, j2, ct + 1);
                )
            ;
        end; 
    done;

    (* Separate output *)
    Printf.printf "-------\n";
) inp;;

Printf.printf "\nPart 2:\n";;
(* Part 2 *)
List.iter ~f:(fun s ->
    (* Code goes here *)
    let grid = s
        |> String.split_on_chars ~on:['\n']
        |> List.filter_map ~f:(fun s -> 
            let l = String.length s in
            if l = 0 then
                None
            else
                Some (Array.init l ~f:(fun i ->
                    s.[i]
                ))
        )
        |> Array.of_list
    in
    let (n, m) = (Array.length grid, Array.length grid.(0)) in
    let shortest = ref 1000000 in 
    find_cells grid n m 'a'
        |> List.iter ~f:(fun (si, sj) ->
            let seen = Array.make_matrix ~dimx:n ~dimy:m false in
            let q = Queue.create () in
            Queue.enqueue q (si, sj, 0);
            while Queue.length q > 0 do
                let (i, j, ct) = Queue.dequeue_exn q in
                if not (seen.(i).(j)) then begin
                    seen.(i).(j) <- true;
                    if Char.equal grid.(i).(j) 'E' then begin
                        shortest := min !shortest ct;
                    end;
                    
                    (neighbors grid i j)
                        |> List.iter ~f:(fun (i2, j2) ->
                            Queue.enqueue q (i2, j2, ct + 1);
                        )
                    ;
                end; 
            done;
        )
    ;
    
    Printf.printf "%d\n" !shortest;

    (* Separate output *)
    Printf.printf "-------\n";
) inp;;

Printf.printf "\nPart 2:\n";;
