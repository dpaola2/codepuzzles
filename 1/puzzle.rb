def count_arara(n)
  if n == 1
    "anane"
  elsif n == 2
    "adak"
  else
    if (n % 2) == 0
      "#{count_arara(n-2)} #{count_arara(2)}"
    else
      "#{count_arara(n-1)} #{count_arara(1)}"
    end
  end
end