open Core;;
include Lib;;

Printf.printf "\n";;

(* Edit this with the correct day *)
let inp = 
    [Common.read_input "./bin/1/sample.txt";
     Common.read_input "./bin/1/input.txt"]
;;

(* Part 1 *)
List.iter ~f:(fun s ->
    (* WRITE CODE HERE - input is "s" *)
    (String.split_on_chars ~on:['\n'] s)
        |> List.filter ~f:(fun s -> String.length s > 0)
        |> List.map ~f:int_of_string
        |> List.fold_left ~init:(1000000,0) ~f:(fun (prev, acc) cur ->
            if prev < cur then
                (cur, acc + 1)
            else
                (cur, acc)
        )
        |> (fun (_, ret) -> Printf.printf "%d\n" ret)
    ;

    (* Separate sample and actual output *)
    Printf.printf "-----\n";
) inp;;

(* Part 2 *)
List.iter ~f:(fun s ->
    (* WRITE CODE HERE - input is "s" *)
    let a = 
      (String.split_on_chars ~on:['\n'] s)
        |> List.filter ~f:(fun s -> String.length s > 0)
        |> List.map ~f:int_of_string
        |> Array.of_list
    in
    let l = Array.length a
    in
    a
        |> Array.mapi ~f:(fun i x -> 
            x + 
            (if i + 1 < l then a.(i+1) else 0) + 
            (if i + 2 < l then a.(i+2) else 0)
        )
        |> Array.fold ~init:(1000000,0) ~f:(fun (prev, acc) cur ->
            if prev < cur then
                (cur, acc + 1)
            else
                (cur, acc)
        )
        |> (fun (_, ret) -> Printf.printf "%d\n" ret)
    ;

    (* Separate sample and actual output *)
    Printf.printf "-----\n";
) inp;;
