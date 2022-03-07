\version "2.22.2" % version
% header
\header{
  title = "欢乐颂"
  composer = "贝多芬曲"
  tagline = ##f % To remove the footer section of the default footer information
  opus = "op.9" % opus number
}
\relative c'{
  \clef "treble"
  \key c \major
  \time 4/4 % time signature
  \tempo 4=130 % the speed or rhythm of a piece of music
  e4 e f g | g f e d     | c c d e     | e4. d8 d2  | \break
  e4 e f g | g f e d     | c c d e     | e4. c8 c2  | \break
  d4 d e c | d e8 f e4 c | d e8 f e4 d | c d g, e'~ | \break
  e e f g  | g f e d     | c c d e     | e4. c8 c2  |  \break
  d4 d e c | d e8 f e4 c | d e8 f e4 d | c d g, e'~ | \break
  e e f g  | g f e d     | c c d e     | d4. c8 c2  | \bar "|."
}
%{\relative c' {
  \clef "treble"
  c1
  \clef "alto"
  c1
  \clef "tenor"
  c1
  \clef "bass"
  c1
}
%\relative c'' {
  \time 3/4
  \tempo "Andante"
  a4 a a
  \time 6/8
  \tempo 4. = 96
  a4. a
  \time 4/4
  \tempo  "Presto" 4 = 120
  a4 a a a
}
% pitch : c,, c, c c' c''
% barline: |  || \bar"|."