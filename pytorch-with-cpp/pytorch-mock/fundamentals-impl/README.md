# `std::vector` Template Type Deduction Guide

[![wakatime](https://wakatime.com/badge/user/f89598ea-6723-481b-a51b-6323e54a3c5c/project/d45ff413-cb36-46d9-ac31-4036f3728c7d.svg)][wakatime_project_status]

```c++
namespace std
{

template<typename T>
vector(initializer_list<T>) -> vector<T>;

template<typename InputIterator,
         typename = std::enable_if_t<
             std::is_constructible_v<T, typename std::iterator_traits<InputIterator>::value_type>
         >>
vector(InputIterator, InputIterator) -> vector<typename std::iterator_traits<InputIterator>::value_type>;

template<typename... Args,
         typename = std::enable_if_t<
             (sizeof...(Args) > 1) &&
             (std::conjunction_v<std::is_same<Args, T>...> || std::conjunction_v<std::is_convertible<Args, T>...>)
         >>
vector(Args&&...) -> vector<T>;

}
```

[wakatime_project_status]: https://wakatime.com/badge/user/f89598ea-6723-481b-a51b-6323e54a3c5c/project/d45ff413-cb36-46d9-ac31-4036f3728c7d
