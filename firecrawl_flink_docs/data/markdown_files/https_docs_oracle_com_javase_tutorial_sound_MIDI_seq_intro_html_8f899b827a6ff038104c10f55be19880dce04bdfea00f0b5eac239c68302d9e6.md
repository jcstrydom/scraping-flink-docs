Documentation

The Java™ Tutorials

Hide TOC

[Overview of the Sampled Package](https://docs.oracle.com/javase/tutorial/sound/sampled-overview.html)

[Accessing Audio System Resources](https://docs.oracle.com/javase/tutorial/sound/accessing.html)

[Playing Back Audio](https://docs.oracle.com/javase/tutorial/sound/playing.html)

[Capturing Audio](https://docs.oracle.com/javase/tutorial/sound/capturing.html)

[Processing Audio with Controls](https://docs.oracle.com/javase/tutorial/sound/controls.html)

[Using Files and Format Converters](https://docs.oracle.com/javase/tutorial/sound/converters.html)

[Overview of the MIDI Package](https://docs.oracle.com/javase/tutorial/sound/overview-MIDI.html)

[Accessing MIDI System Resources](https://docs.oracle.com/javase/tutorial/sound/accessing-MIDI.html)

[Transmitting and Receiving MIDI Messages](https://docs.oracle.com/javase/tutorial/sound/MIDI-messages.html)

Introduction to Sequencers

[Using Sequencer Methods](https://docs.oracle.com/javase/tutorial/sound/MIDI-seq-methods.html)

[Using Advanced Sequencer Features](https://docs.oracle.com/javase/tutorial/sound/MIDI-seq-adv.html)

[Synthesizing Sound](https://docs.oracle.com/javase/tutorial/sound/MIDI-synth.html)

[Introduction to the Service Provider Interfaces](https://docs.oracle.com/javase/tutorial/sound/SPI-intro.html)

[Providing Sampled-Audio Services](https://docs.oracle.com/javase/tutorial/sound/SPI-providing-sampled.html)

[Providing MIDI Services](https://docs.oracle.com/javase/tutorial/sound/SPI-providing-MIDI.html)

**Trail:** Sound


[Home Page](https://docs.oracle.com/javase/tutorial/index.html)
>
[Sound](https://docs.oracle.com/javase/tutorial/sound/index.html)

[« Previous](https://docs.oracle.com/javase/tutorial/sound/MIDI-messages.html) • [Trail](https://docs.oracle.com/javase/tutorial/sound/TOC.html) • [Next »](https://docs.oracle.com/javase/tutorial/sound/MIDI-seq-methods.html)

The Java Tutorials have been written for JDK 8. Examples and practices described in this page don't take advantage of improvements introduced in later releases and might use technology no longer available.

See [Dev.java](https://dev.java/learn/) for updated tutorials taking advantage of the latest releases.

See [Java Language Changes](https://docs.oracle.com/pls/topic/lookup?ctx=en/java/javase&id=java_language_changes) for a summary of updated language features in Java SE 9 and subsequent releases.

See [JDK Release Notes](https://www.oracle.com/technetwork/java/javase/jdk-relnotes-index-2162236.html) for information about new features, enhancements, and removed or deprecated options for all JDK releases.

# Introduction to Sequencers

In the world of MIDI, a _sequencer_ is any hardware or software device that can precisely play or record a _sequence_ of time-stamped MIDI messages. Similarly, in the Java Sound API, the
[`Sequencer`](https://docs.oracle.com/javase/8/docs/api/javax/sound/midi/Sequencer.html) abstract interface defines the properties of an object that can play and record sequences of
[`MidiEvent`](https://docs.oracle.com/javase/8/docs/api/javax/sound/midi/MidiEvent.html) objects. A `Sequencer` typically loads these `MidiEvent` sequences from a standard MIDI file or saves them to such a file. Sequences can also be edited. The following pages explain how to use `Sequencer` objects, along with related classes and interfaces, to accomplish such tasks.

To develop an intuitive understanding of what a `Sequencer` is, think of it by analogy with a tape recorder, which a sequencer resembles in many respects. Whereas a tape recorder plays audio, a sequencer plays MIDI data. A sequence is a multi-track, linear, time-ordered recording of MIDI musical data, which a sequencer can play at various speeds, rewind, shuttle to particular points, record into, or copy to a file for storage.

[Transmitting and Receiving MIDI Messages](https://docs.oracle.com/javase/tutorial/sound/MIDI-messages.html) explained that devices typically have `Receiver` objects, `Transmitter` objects, or both. To _play_ music, a device generally receives `MidiMessages` through a `Receiver`, which in turn has usually received them from a `Transmitter` that belongs to a `Sequencer`. The device that owns this `Receiver` might be a `Synthesizer`, which will generate audio directly, or it might be a MIDI output port, which transmits MIDI data through a physical cable to some external piece of equipment. Similarly, to _record_ music, a series of time-stamped `MidiMessages` are generally sent to a `Receiver` owned by a `Sequencer`, which places them in a `Sequence` object. Typically the object sending the messages is a `Transmitter` associated with a hardware input port, and the port relays MIDI data that it gets from an external instrument. However, the device responsible for sending the messages might instead be some other `Sequencer`, or any other device that has a `Transmitter`. Furthermore, as previously described, a program can send messages without using any `Transmitter` at all.

A `Sequencer` itself has both `Receivers` and `Transmitters`. When it's recording, it actually obtains `MidiMessages` via its `Receivers`. During playback, it uses its `Transmitters` to send `MidiMessages` that are stored in the `Sequence` that it has recorded (or loaded from a file).

One way to think of the role of a `Sequencer` in the Java Sound API is as an aggregator and "de-aggregator" of `MidiMessages`. A series of separate `MidiMessages`, each of which is independent, is sent to the `Sequencer` along with its own time stamp that marks the timing of a musical event. These `MidiMessages` are encapsulated in `MidiEvent` objects and collected in `Sequence` objects through the action of the `Sequencer.record` method. A `Sequence` is a data structure containing aggregates of `MidiEvents`, and it usually represents a series of musical notes, often an entire song or composition. On playback, the `Sequencer` again extracts the `MidiMessages` from the `MidiEvent` objects in the `Sequence` and then transmits them to one or more devices that will either render them into sound, save them, modify them, or pass them on to some other device.

Some sequencers might have neither transmitters nor receivers. For example, they might create `MidiEvents` from scratch as a result of keyboard or mouse events, instead of receiving `MidiMessages` through `Receivers`. Similarly, they might play music by communicating directly with an internal synthesizer (which could actually be the same object as the sequencer) instead of sending `MidiMessages` to a `Receiver` associated with a separate object. However, the rest of this discussion assumes the normal case of a sequencer that uses `Receivers` and `Transmitters`.

## When to Use a Sequencer

It's possible for an application program to send MIDI messages directly to a device, without using a sequencer, as was described in
[Transmitting and Receiving MIDI Messages](https://docs.oracle.com/javase/tutorial/sound/MIDI-messages.html). The program simply invokes the `Receiver.send` method each time it wants to send a message. This is a straightforward approach that's useful when the program itself creates the messages in real time. For example, consider a program that lets the user play notes by clicking on an onscreen piano keyboard. When the program gets a mouse-down event, it immediately sends the appropriate Note On message to the synthesizer.

As previously mentioned, the program can include a time stamp with each MIDI message it sends to the device's receiver. However, such time stamps are used only for fine-tuning the timing, to correct for processing latency. The caller can't generally set arbitrary time stamps; the time value passed to `Receiver.send` must be close to the present time, or the receiving device might not be able to schedule the message correctly. This means that if an application program wanted to create a queue of MIDI messages for an entire piece of music ahead of time (instead of creating each message in response to a real-time event), it would have to be very careful to schedule each invocation of `Receiver.send` for nearly the right time.

Fortunately, most application programs don't have to be concerned with such scheduling. Instead of invoking `Receiver.send` itself, a program can use a `Sequencer` object to manage the queue of MIDI messages for it. The sequencer takes care of scheduling and sending the messages—in other words, playing the music with the correct timing. Generally, it's advantageous to use a sequencer whenever you need to convert a non-real-time series of MIDI messages to a real-time series (as in playback), or vice versa (as in recording). Sequencers are most commonly used for playing data from MIDI files and for recording data from a MIDI input port.

## Understanding Sequence Data

Before examining the `Sequencer` API, it helps to understand the kind of data that's stored in a sequence.

### Sequences and Tracks

In the Java Sound API, sequencers closely follow the Standard MIDI Files specification in the way that they organize recorded MIDI data. As mentioned above, a `Sequence` is an aggregation of `MidiEvents`, organized in time. But there is more structure to a `Sequence` than just a linear series of `MidiEvents`: a `Sequence` actually contains global timing information plus a collection of `Tracks`, and it is the `Tracks` themselves that hold the `MidiEvent` data. So the data played by a sequencer consists of a three-level hierarchy of objects: `Sequencer`, `Track`, and `MidiEvent`.

In the conventional use of these objects, the `Sequence` represents a complete musical composition or section of a composition, with each `Track` corresponding to a voice or player in the ensemble. In this model, all the data on a particular `Track` would also therefore be encoded into a particular MIDI channel reserved for that voice or player.

This way of organizing data is convenient for purposes of editing sequences, but note that this is just a conventional way to use `Tracks`. There is nothing in the definition of the `Track` class that keeps it from containing a mix of `MidiEvents` on different MIDI channels. For example, an entire multi-channel MIDI composition can be mixed and recorded onto one `Track`. Also, standard MIDI files of Type 0 (as opposed to Type 1 and Type 2) contain by definition only one track; so a `Sequence` that's read from such a file will necessarily have a single `Track` object.

### MidiEvents and Ticks

As discussed in
[Overview of the MIDI Package](https://docs.oracle.com/javase/tutorial/sound/overview-MIDI.html), the Java Sound API includes `MidiMessage` objects that correspond to the raw two- or three-byte sequences that make up most standard MIDI messages. A `MidiEvent` is simply a packaging of a `MidiMessage` along with an accompanying timing value that specifies when the event occurs. (We might then say that a sequence really consists of a four- or five-level hierarchy of data, rather than three-level, because the ostensible lowest level, `MidiEvent`, actually contains a lower-level `MidiMessage`, and likewise the `MidiMessage` object contains an array of bytes that comprises a standard MIDI message.)

In the Java Sound API, there are two different ways in which `MidiMessages` can be associated with timing values. One is the way mentioned above under "When to Use a Sequencer." This technique was described in detail under
[Sending a Message to a Receiver without Using a Transmitter](https://docs.oracle.com/javase/tutorial/sound/MIDI-messages.html#sending) and
[Understanding Time Stamps](https://docs.oracle.com/javase/tutorial/sound/MIDI-messages.html#understanding_time). There, we saw that the `send` method of `Receiver` takes a `MidiMessage` argument and a time-stamp argument. That kind of time stamp can only be expressed in microseconds.

The other way in which a `MidiMessage` can have its timing specified is by being encapsulated in a `MidiEvent`. In this case, the timing is expressed in slightly more abstract units called _ticks_.

What is the duration of a tick? It can vary between sequences (but not within a sequence), and its value is stored in the header of a standard MIDI file. The size of a tick is given in one of two types of units:

- Pulses (ticks) per quarter note, abbreviated as PPQ
- Ticks per frame, also known as SMPTE time code (a standard adopted by the Society of Motion Picture and Television Engineers)

If the unit is PPQ, the size of a tick is expressed as a fraction of a quarter note, which is a relative, not absolute, time value. A quarter note is a musical duration value that often corresponds to one beat of the music (a quarter of a measure in 4/4 time). The duration of a quarter note is dependent on the tempo, which can vary during the course of the music if the sequence contains tempo-change events. So if the sequence's timing increments (ticks) occur, say 96 times per quarter note, each event's timing value measures that event's position in musical terms, not as an absolute time value.

On the other hand, in the case of SMPTE, the units measure absolute time, and the notion of tempo is inapplicable. There are actually four different SMPTE conventions available, which refer to the number of motion-picture frames per second. The number of frames per second can be 24, 25, 29.97, or 30. With SMPTE time code, the size of a tick is expressed as a fraction of a frame.

In the Java Sound API, you can invoke `Sequence.getDivisionType` to learn which type of unit—namely, PPQ or one of the SMPTE units—is used in a particular sequence. You can then calculate the size of a tick after invoking `Sequence.getResolution`. The latter method returns the number of ticks per quarter note if the division type is PPQ, or per SMPTE frame if the division type is one of the SMPTE conventions. You can get the size of a tick using this formula in the case of PPQ:

```
ticksPerSecond =
    resolution * (currentTempoInBeatsPerMinute / 60.0);
tickSize = 1.0 / ticksPerSecond;
```

and this formula in the case of SMPTE:

```
framesPerSecond =
  (divisionType == Sequence.SMPTE_24 ? 24
    : (divisionType == Sequence.SMPTE_25 ? 25
      : (divisionType == Sequence.SMPTE_30 ? 30
        : (divisionType == Sequence.SMPTE_30DROP ?

            29.97))));
ticksPerSecond = resolution * framesPerSecond;
tickSize = 1.0 / ticksPerSecond;
```

The Java Sound API's definition of timing in a sequence mirrors that of the Standard MIDI Files specification. However, there's one important difference. The tick values contained in `MidiEvents` measure _cumulative_ time, rather than _delta_ time. In a standard MIDI file, each event's timing information measures the amount of time elapsed since the onset of the previous event in the sequence. This is called delta time. But in the Java Sound API, the ticks aren't delta values; they're the previous event's time value _plus_ the delta value. In other words, in the Java Sound API the timing value for each event is always greater than that of the previous event in the sequence (or equal, if the events are supposed to be simultaneous). Each event's timing value measures the time elapsed since the beginning of the sequence.

To summarize, the Java Sound API expresses timing information in either MIDI ticks or microseconds. `MidiEvents` store timing information in terms of MIDI ticks. The duration of a tick can be calculated from the `Sequence's` global timing information and, if the sequence uses tempo-based timing, the current musical tempo. The time stamp associated with a `MidiMessage` sent to a `Receiver`, on the other hand, is always expressed in microseconds.

One goal of this design is to avoid conflicting notions of time. It's the job of a `Sequencer` to interpret the time units in its `MidiEvents`, which might have PPQ units, and translate these into absolute time in microseconds, taking the current tempo into account. The sequencer must also express the microseconds relative to the time when the device receiving the message was opened. Note that a sequencer can have multiple transmitters, each delivering messages to a different receiver that might be associated with a completely different device. You can see, then, that the sequencer has to be able to perform multiple translations at the same time, making sure that each device receives time stamps appropriate for its notion of time.

To make matters more complicated, different devices might update their notions of time based on different sources (such as the operating system's clock, or a clock maintained by a sound card). This means that their timings can drift relative to the sequencer's. To keep in synchronization with the sequencer, some devices permit themselves to be "slaves" to the sequencer's notion of time. Setting masters and slaves is discussed later under
[`MidiEvent`](https://docs.oracle.com/javase/8/docs/api/javax/sound/midi/MidiEvent.html).

[« Previous](https://docs.oracle.com/javase/tutorial/sound/MIDI-messages.html)
•
[Trail](https://docs.oracle.com/javase/tutorial/sound/TOC.html)
•
[Next »](https://docs.oracle.com/javase/tutorial/sound/MIDI-seq-methods.html)

* * *

[About Oracle](https://www.oracle.com/corporate/) \|
[Contact Us](https://www.oracle.com/corporate/contact/) \|
[Legal Notices](https://www.oracle.com/legal/) \|
[Terms of Use](https://www.oracle.com/legal/terms.html) \|
[Your Privacy Rights](https://www.oracle.com/legal/privacy/)

[Copyright © 1995, 2024 Oracle and/or its affiliates. All rights reserved.](http://www.oracle.com/pls/topic/lookup?ctx=cpyr&id=en-US)

**Previous page:** Transmitting and Receiving MIDI Messages


**Next page:** Using Sequencer Methods


- [Ad Choices](https://www.oracle.com/legal/privacy/marketing-cloud-data-cloud-privacy-policy.html#12)