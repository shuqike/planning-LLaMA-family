(define (problem BW-generalization-4)
(:domain blocksworld-4ops)(:objects i d h e a j)
(:init 
(handempty)
(ontable i)
(ontable d)
(ontable h)
(ontable e)
(ontable a)
(ontable j)
(clear i)
(clear d)
(clear h)
(clear e)
(clear a)
(clear j)
)
(:goal
(and
(on i d)
(on d h)
(on h e)
(on e a)
(on a j)
)))