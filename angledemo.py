import math

import angle


def main():

    print("-----------------")
    print("| codedrome.com |")
    print("| Angles        |")
    print("-----------------\n")

    create_and_output()

    # set_value()

    # arithmetic()

    # comparisons()

    # approx_equal()

    # convert_units()


def create_and_output():

    dms = angle.Angle((27,14,33), angle.Angle.units["degreeminutesecond"])
    print(dms.unit["name"])
    print(f"seconds      {dms.seconds}")
    print(f"value        {dms.value}")
    print(f"__str__      {dms}")

    print()

    r = angle.Angle(2 * math.pi, angle.Angle.units["radian"])
    print(r.unit["name"])
    print(f"seconds      {r.seconds}")
    print(f"value        {r.value}")
    print(f"__str__      {r}")

    print()

    g = angle.Angle(400, angle.Angle.units["gradian"])
    print(g.unit["name"])
    print(f"seconds      {g.seconds}")
    print(f"value        {g.value}")
    print(f"__str__      {g}")

    print()

    t = angle.Angle(1, angle.Angle.units["turn"])
    print(t.unit["name"])
    print(f"seconds      {t.seconds}")
    print(f"value        {t.value}")
    print(f"__str__      {t}")

    print()

    ha = angle.Angle(24, angle.Angle.units["hourangle"])
    print(ha.unit["name"])
    print(f"seconds      {ha.seconds}")
    print(f"value        {ha.value}")
    print(f"__str__      {ha}")

    print()

    p = angle.Angle(32, angle.Angle.units["point"])
    print(p.unit["name"])
    print(f"seconds      {p.seconds}")
    print(f"value        {p.value}")
    print(f"__str__      {p}")

    print()

    q = angle.Angle(4, angle.Angle.units["quadrant"])
    print(q.unit["name"])
    print(f"seconds      {q.seconds}")
    print(f"value        {q.value}")
    print(f"__str__      {q}")


def set_value():

    dms = angle.Angle((7,12,39), angle.Angle.units["degreeminutesecond"])
    print(dms)

    dms.value = (29,45,12)
    print(dms)


def arithmetic():

    dms = angle.Angle((45,0,0), angle.Angle.units["degreeminutesecond"])
    q = angle.Angle(1, angle.Angle.units["quadrant"])

    dms_plus_q = dms + q
    q_minus_dms = q - dms
    dms_times_two = dms * 2
    three_times_dms = 3 * dms
    dms_div_nine = dms / 9

    print(f"dms              {dms}")
    print(f"q                {q}")

    print()

    print(f"dms_plus_q       {dms_plus_q}")
    print(f"q_minus_dms      {q_minus_dms}")
    print(f"dms_times_two    {dms_times_two}")
    print(f"three_times_dms  {three_times_dms}")
    print(f"dms_div_nine     {dms_div_nine}")


def comparisons():

    dms = angle.Angle((90,0,0), angle.Angle.units["degreeminutesecond"])
    q = angle.Angle(1, angle.Angle.units["quadrant"])
    r = angle.Angle(1, angle.Angle.units["radian"])

    print(f"{r} < {dms}   = {r < dms}")
    print(f"{dms} <= {q} = {dms <= q}")
    print(f"{dms} == {r}  = {dms == r}")
    print(f"{dms} > {r}   = {dms > r}")
    print(f"{q} >= {dms} = {q >= dms}")
    print(f"{r} != {dms}  = {r != dms}")


def approx_equal():

    dms = angle.Angle((360,0,0), angle.Angle.units["degreeminutesecond"])
    r = angle.Angle(2 * math.pi, angle.Angle.units["radian"])

    print(f"dms.seconds           {dms.seconds}")
    print(f"r.seconds             {r.seconds}")
    print(f"dms == r              {dms == r}")

    print()

    dms = dms / 3
    r = r / 3

    print(f"dms.seconds           {dms.seconds}")
    print(f"r.seconds             {r.seconds}")
    print(f"dms == r              {dms == r}")
    print(f"dms.approx_equal(r)   {dms.approx_equal(r)}")


def convert_units():

    right_angle = angle.Angle((90,0,0), angle.Angle.units["degreeminutesecond"])
    print(right_angle.unit["name"])
    print(right_angle)

    print()

    right_angle.unit = angle.Angle.units["quadrant"]
    print(right_angle.unit["name"])
    print(right_angle)

    print()

    right_angle.unit = angle.Angle.units["gradian"]
    print(right_angle.unit["name"])
    print(right_angle)


if __name__ == "__main__":

    main()
