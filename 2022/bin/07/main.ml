open Core;;
include Lib;;

Printf.printf "\n";;
Printf.printf "Part 1:\n";;

(* Edit this with the correct day *)
let inp = 
    [Common.read_input "./bin/07/sample.txt";
     Common.read_input "./bin/07/input.txt"]
;;

let contains target search =
    String.substr_index ~pattern:search target
        |> fun o -> not (Option.is_none o)
;;

(* I recognize this is not exhaustive, a non-directory file could have
 * the substring "dir" in it which would cause this to fail, but idc right now
 *)
let node_type s =
    let l = String.length s in
    if contains s "$ cd" then
        ("cd", String.sub ~pos:5 ~len:(l - 5) s)
    else if contains s "$ ls" then
        ("none", "")
    else if contains s "dir" then
        ("none", "")
    else 
        let blank = String.index_exn s ' ' in
        ("size", String.sub ~pos:0 ~len:blank s)
;;

(* dfs recursively calculates the sum of all qualifying
 * directories. it returns (v, node) where v is the sum
 * of qualifying nodes under the current node, and "node" is
 * the next node that the parent should look at  
 *)
let rec dfs index arr = match index with
    | i                ->
        let ret = ref 0 in
        let cur = ref 0 in
        let j = ref i in
        let stay = ref true in
        let go_back = ref false in
        (* stay here as long as we are still in this directory *) 
        while !stay do
            let cmd, arg = node_type arr.(!j) in (
            match cmd with
                | "cd"   -> (
                    match arg with
                        | ".." ->
                            stay := false;
                        | "/"  ->
                            if index <> 0 then (
                                stay := false;
                                go_back := true;
                            )
                        | _  ->
                            let (this_ret, this, nj, gb) = dfs (!j+1) arr in
                            j := nj - 1;
                            cur := !cur + this;
                            ret := !ret + this_ret;
                            go_back := gb;
                );
                | "size" ->
                    let int_arg = int_of_string arg in
                    cur := !cur + int_arg;
                | _      -> 
                    j := !j + 0; (* noop *)
            );

            j := !j + 1;
            stay := (!j < Array.length arr) && !stay;
        done;

        if !cur <= 100_000 then
            ret := !ret + !cur;

        (!ret, !cur, !j, !go_back) 
;;


(* Part 1 *)
List.iteri ~f:(fun _ s ->
    (* Code goes here *)
    s
        |> String.split_on_chars ~on:['\n']
        |> List.filter ~f:(fun s -> String.length s > 0)
        |> Array.of_list
        |> dfs 0
        |> fun (ret, _, _, _) -> Printf.printf "%d\n" ret
    ;
    
    (* Separate output *)
    Printf.printf "-------\n";
) inp;;

Printf.printf "\nPart 2:\n";;

let used = [|48381165; 42476859|];;

(* dfs2 does exactly what dfs does, except it returns the min
 * file size above the amount of space needed instead. I would
 * have just modified that function, but I want to keep record
 * of all the code I used even if it means duplicating it
 *)
let rec dfs2 index arr = match index with
    | i                ->
        let need = 30_000_000 - (70_000_000 - used.(if Array.length arr < 30 then 0 else 1)) in
        let ret = ref 1_000_000_000 in
        let cur = ref 0 in
        let j = ref i in
        let stay = ref true in
        let go_back = ref false in
        (* stay here as long as we are still in this directory *) 
        while !stay do
            let cmd, arg = node_type arr.(!j) in (
            match cmd with
                | "cd"   -> (
                    match arg with
                        | ".." ->
                            stay := false;
                        | "/"  ->
                            if index <> 0 then (
                                stay := false;
                                go_back := true;
                            )
                        | _  ->
                            let (this_ret, this, nj, gb) = dfs2 (!j+1) arr in
                            j := nj - 1;
                            cur := !cur + this;
                            ret := min !ret this_ret;
                            go_back := gb;
                );
                | "size" ->
                    let int_arg = int_of_string arg in (
                    cur := !cur + int_arg;
                )
                | _      -> 
                    j := !j + 0; (* noop *)
            );

            j := !j + 1;
            stay := (!j < Array.length arr) && !stay;
        done;

        if !cur >= need then
            ret := min (!ret) (!cur);

        (!ret, !cur, !j, !go_back) 
;;
(* Part 2 *)
List.iteri ~f:(fun _ s ->
    (* Code goes here *)
    s
        |> String.split_on_chars ~on:['\n']
        |> List.filter ~f:(fun s -> String.length s > 0)
        |> Array.of_list
        |> dfs2 0
        |> fun (ret, _, _, _) -> Printf.printf "%d\n" ret
    ;
    
    (* Separate output *)
    Printf.printf "-------\n";
) inp;;
