(define (problem BW-generalization-4)
(:domain blocksworld-4ops)(:objects h a b l e f i d g k j)
(:init 
(handempty)
(ontable h)
(ontable a)
(ontable b)
(ontable l)
(ontable e)
(ontable f)
(ontable i)
(ontable d)
(ontable g)
(ontable k)
(ontable j)
(clear h)
(clear a)
(clear b)
(clear l)
(clear e)
(clear f)
(clear i)
(clear d)
(clear g)
(clear k)
(clear j)
)
(:goal
(and
(on h a)
(on a b)
(on b l)
(on l e)
(on e f)
(on f i)
(on i d)
(on d g)
(on g k)
(on k j)
)))