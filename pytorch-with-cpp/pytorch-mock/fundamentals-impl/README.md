# `std::vector` Template Type Deduction Guide

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
