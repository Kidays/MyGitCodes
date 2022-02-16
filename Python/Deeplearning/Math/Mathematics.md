## Function definition
- Relationship between variables:$A=\pi r^2$
- $y=f(x)$ x:independent variable;y:dependent variable
- $y_0=y|_{x=x_0}=f(x_0)$
## Types
- Piecewise function:$f(x)=\begin{cases}\sqrt{x},x\geq 0\\-x,x\leq 0\end{cases}$
- Inverse function:$h=\frac{1}{2}gt^2\rightarrow \underline{h}=\underline{h}(t)\quad t=\sqrt{\frac{2h}{g}}\quad \rightarrow t=t(h)$
- Explicit function & implicit function:$y=x^2+1\quad F(x,y)=0$
## Property
- Parity:
  even function:$f(-x)=f(x) \quad f(x)=x^2$
  odd function:$f(-x)=-f(x) \quad f(x)=x^3$
- Periodically:
  $f(x+T)=f(x)$
- Monotonicity:increasing and decreasing function
## Limit
- $\lim\limits_{n\to\infty}u_n=A \quad u_n\rightarrow A(n\rightarrow\infty)$
  $\lim\limits_{n\to\infty}\frac{1}{3^n}=0\quad\lim\limits_{n\to\infty}\frac{n}{n+1}=1$
- Symbol:$x\rightarrow x_0^+$: close to the right
  $\lim\limits_{x\to\infty}e^{-x}=0$
  $\lim\limits_{x\to-\infty}arctan x=-\frac{\pi}{2}$
- sufficient and necessary condition
  $\lim\limits_{x\to x_0}f(x)=A:\quad\lim\limits_{x\to x_0^-}f(x)=\lim\limits_{x\to x_0^+}f(x)=A$
## The continuity of function
  $\lim\limits_{\Delta x\to 0}\Delta y=\lim\limits_{\Delta x\to 0}[f(x_0+\Delta x)-f(x_0)]=0$
## Derivative
- $\lim\limits_{\Delta x\to 0}\frac{\Delta y}{\Delta x}=\lim\limits_{\Delta x \to 0}\frac{f(x_0+\Delta x)-f(x_0)}{\Delta x}$
- $f^{'}(x_0)\quad y^{'}|_{x=x_0}\quad \frac{dy}{dx}|_{x=x_0}\quad \frac{df(x)}{dx}|_{x=x_0}$
- $(C)'=0\quad (x^\mu)'=\mu\cdot x^{\mu-1}$
  $(sin x)'=cos x\quad (cos x)'=-sin x$
  $(a^x)'=a^x ln a\quad (e^x)'=e^x$
  $(log_a x)'=\frac{1}{x ln a}\quad (ln x)'=\frac{1}{x}$
- $(u\pm v)'=u'\pm v'\quad (uv)'=u'v+uv'$
  $(\frac{u}{v})'=\frac{u'v-uv'}{v^2}(v\neq0)$
## Partial Derivative
- $y=y_0$
  $z=f(x,y)$
  $x_0,y_0$
  $f_x (x_0,y_0)=\frac{\partial z}{\partial x}|_{\begin{smallmatrix} x=x_0 \\ y=y_0\end{smallmatrix}}=\frac{\partial f}{\partial x}|_{\begin{smallmatrix} x=x_0\\ y=y_0\end{smallmatrix}}=z_x|_{\begin{smallmatrix} x=x_0\\ y=y_0\end{smallmatrix}}$
## Gradient
- Directional derivative
  $\frac{\partial f}{\partial l}=\frac{\partial f}{\partial  x}cos{\varphi}+\frac{\partial f}{\partial y}sin {\varphi}=\{\frac{\partial f}{\partial x},\frac{\partial f}{\partial y}\}\cdot\{cos{\varphi},sin{\varphi}\}$
  $=gradf(x,y)\cdot\overrightarrow{e}=|gradf(x,y)|cos\theta$
  $\varphi$: angle of x l
  $\overrightarrow{e}=cos\varphi \overrightarrow{i}+sin\varphi\overrightarrow{j}$: unit vector
  $\theta=(gradf(x,y),\overrightarrow{e})$
- Example
  $u=xyz+z^2+5\quad\rightarrow\quad grad\ u$
  $\because\quad\frac{\partial u}{\partial x}=yz,\quad\frac{\partial u}{\partial y}=xz,\quad\frac{\partial u}{\partial z}=xy+2z$
  $\therefore\quad grad\ u|_{(0,1,-1)}=(yz,xz,xy+2z)|_{(0,1,-1)}=(-1,0,-2)$
  $max\{\frac{\partial u}{\partial l}|_M\}=\|grad\ u\|=\sqrt5$
  $min\{\frac{\partial u}{\partial l}|_M\}=-\|grad\ u\|=-\sqrt5$
## Calculus
- $Sum(f(x)\Delta x)\Rightarrow\int f(x)dx$
  $f'(x)=\frac{dy}{dx}$
  $\Delta x=dx\quad\Delta y=dy+o (\Delta x)$
  $\int_a^bf(x)dx=\lim\limits_{\lambda\rightarrow 0}\sum_{i=1}^nf(\xi)\Delta x_i$
- The first Mean Value Theorem
  $[a,b]\quad(a\leq\xi\leq b)$
  $\int_a^bf(x)dx=f(\xi)(b-a)$
- Newton - leibniz formula
  $\int_a^bf(x)dx=F(b)-F(a)\quad Primitive function:F(x)$
- Example
  $\int_0^{\frac{\pi}{2}}(2cos\ x+sin\ x-1)dx$
  $[2sin\ x-cos\ x-x]_0^{\frac{\pi}{2}}=3-\frac{\pi}{2}$
- $f(x)\in C[a,b],F'(x)=f(x)$
  $\int_a^bf(x)dx=f(\xi)(b-a)=F'(\xi)(b-a)=F(b)-F(a)$
## Taylor's formula
  $f(x)=f(x_0)+f'(x_0)(x-x_0)+o(x-x_0)$
  $f(x)\approx f(x_0)+f'(x_0)(x-x_0)$
  Intersect: $P_n(x_0)=f(x_0)$
  The same tangent: $P_n'(x_0)=f'(x_0)$
  Bending the same direction: $P_n''(x_0)=f''(x_0)$
- $P_n(x)=f(x_0)+f'(x_0)(x-x_0)+\frac{f''(x_0)}{2!}(x-x_0)^2+\cdots+\frac{f^{(n)(x_0)}}{n!}(x-x_0)^n$
## Maclaurin formula
  $f(x)=f(0)+f'(0)x+\frac{f''(0)}{2!}x^2+\cdots+\frac{f^{(n)}(0)}{(n!}x^n+\frac{f{(n+1)}(\theta x)}{(n+1)!}x^{n+1}\quad(0<\theta<1)$
  $f(x)\approx f(0)+f'(0)x+\frac{f''(0)}{2!}x^2+\cdots+\frac{f^{(n)}(0)}{n!}x^n$
  $e^x=1+x+\frac{x^2}{2!}+\cdots+\frac{x^n}{n!}+\frac{e^{\theta x}}{(e+1)!}x^{n+1}\quad(0<\theta<1)$
## Extremum value (lagrangian multiplier method)
  $z=f(x,y)$
  $f_x(x,y)=0,f_y(x,y)=0$

  $z=f(x,y),\varphi(x,y)=0$
  $F(x,y)=f(x,y)+\lambda\varphi(x,y)$
$\left\{
\begin{aligned}
f_x(x,y)+\lambda\varphi_x(x,y) & = & 0\\
f_y(x,y)+\lambda\varphi_x(x,y) & = & 0\\
\varphi(x,y) & = & 0
\end{aligned}
\right.
$
